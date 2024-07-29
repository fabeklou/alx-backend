import { createClient } from 'redis';

const subClient = createClient();

subClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

subClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

subClient.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      subClient.unsubscribe();
      subClient.quit();
    }
    console.log(message);
  }
});

subClient.subscribe('holberton school channel');
