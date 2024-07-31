import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect, should } from 'chai';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  const jobs = [{
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '1878041535',
    message: 'This is the code 3412 to verify your account'
  }];

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()
  });

  it('should throw an Error \'Jobs is not an array\'', () => {
    expect(createPushNotificationsJobs.bind(
      createPushNotificationsJobs, 'Not an array', queue))
      .to.throw('Jobs is not an array');
  });

  it('should create two jobs', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should create push_notification_code_3 jobs', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  });

  it('should create job with provided data', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: '1878041535',
      message: 'This is the code 3412 to verify your account'
    });
  });
});
