import kue from 'kue';

const queue = kue.createQueue();

const queueData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', queueData);

job.save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
  console.log('Notification job failed');
});
