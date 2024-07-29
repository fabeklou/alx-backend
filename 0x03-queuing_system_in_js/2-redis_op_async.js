import redis, { createClient } from 'redis';
import util from 'util';

const client = createClient();
const clientGetAsync = util.promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await clientGetAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err.message);
  }
};

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`)
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
