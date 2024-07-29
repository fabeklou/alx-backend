import redis from 'redis';

const pubClient = redis.createClient();

const publishMessage = (message, time) => {
  const channelName = 'holberton school channel';
  setTimeout(() => {
    console.log(`About to send ${message}`);
    pubClient.publish(channelName, message);
  }, time);
};

pubClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

pubClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
