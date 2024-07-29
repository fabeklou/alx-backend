import redis from 'redis';

const client = redis.createClient();

const schools = [
  ['Portland', 50],
  ['Seattle', 80],
  ['New York', 20],
  ['Bogota', 20],
  ['Cali', 40],
  ['Paris', 2]
];

for (const school of schools) {
  const [schoolName, schoolValue] = school;
  client.hset('HolbertonSchools', schoolName, schoolValue, redis.print);
}

client.hgetall('HolbertonSchools', (error, reply) => {
  if (error) throw (error);
  console.log(reply);
});
