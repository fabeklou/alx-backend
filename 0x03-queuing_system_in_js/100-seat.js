import redis from 'redis';
import { promisify } from 'util';
import express from 'express';
import kue from 'kue';

const app = express();
const port = 1245;
const queue = kue.createQueue();

/** Create Redis client */
const client = redis.createClient();
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

/** Initialize reservation status */
let reservationEnabled = true;

/** Reserve seat */
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

/** Get current available seats */
const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats);
};

/** Routes */
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat');

  job.save((error) => {
    if (error) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    if (!reservationEnabled) {
      done(new Error('Not enough seats available'));
    }
    const availableSeats = await getCurrentAvailableSeats();
    await reserveSeat(availableSeats - 1);

    if (availableSeats === 1) reservationEnabled = false;
  });
});

app.listen(port, () => {
  /** Initialize available seats */
  reserveSeat(50);
  console.log(`Server listening on port ${port}`);
});
