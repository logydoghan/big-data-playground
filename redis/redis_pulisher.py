# read from kafka topic
# publish to redis pub

from kafka import KafkaConsumer
from kafka.errors import KafkaError

import redis
import argparse
import logging
import atexit

class redis_publish():

	def __init__(self, topic_name, kafka_broker, redis_channel, redis_host, redis_port):
		self.redis_channel = redis_channel
		self.consumer = KafkaConsumer(topic_name, bootstrap_servers=kafka_broker)
		self.redis_client = redis.StrictRedis(host = redis_host, port = redis_port)
		logging.basicConfig(format='%(asctime)-15s %(message)s')
		self.logger = logging.getLogger('redis_publisher')
		self.logger.setLevel(logging.INFO)

	def shutdown_hook(self):
		try:
			self.consumer.close()
			self.logger.info('Closed kafka consumer')
		except KafkaError as kafka_error:
			self.logger.warn('Failed to close kafka consumer, caused by %s' % kafka_error.message)
		# finally:
		# 	try:
		# 		self.redis_client.shutdown()
		# 		self.logger.info('Redis client closed')
		# 	except Exception as e:
		# 		self.logger.warn('Failed to close redis client, caused by %s' % e.message)

	def publishing(self):
		for msg in self.consumer:
			self.logger.info('Received data from kafka')
			self.redis_client.publish(self.redis_channel, msg.value)
			self.logger.info('Published the message, %s' % msg.value)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('topic_name', help='the kafka topic to consumer')
	parser.add_argument('kafka_broker', help = 'the location of kafka broker')
	parser.add_argument('redis_channel', help = 'the redis channel to publish to')
	parser.add_argument('redis_host')
	parser.add_argument('redis_port')

	args = parser.parse_args()
	topic_name = args.topic_name
	kafka_broker = args.kafka_broker
	redis_channel = args.redis_channel
	redis_host = args.redis_host
	redis_port = args.redis_port

	rp = redis_publish(topic_name, kafka_broker, redis_channel, redis_host, redis_port)
	atexit.register(rp.shutdown_hook)
	rp.publishing()
