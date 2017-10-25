# - read from any kafak
 # - write to any cassandra
 # - get message from kafka write to cassandra
from cassandra.cluster import Cluster
from kafka import KafkaConsumer

import argparse
import logging

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('data-storage')
logger.setLevel(logging.DEBUG)

topic_name = 'stock-analyzer'
kafka_broker = '127.0.0.1:9092'
cassandra_broker = '127.0.0.1'
keyspace = 'stock'
data_table = 'stock_price'

def persist_data(stock_data, cassandra_session):
 	try:
 		logger.debug('start to save data to cassandra %s', stock_data)
 		parsed = json.loads(stock_data)[0]
 		symbol = parsed.get('StockSymbol')
 		price = float(parsed.get('LastTradePrice'))
 		tradetime = parsed.get('LastTradeDatetime')

 		# - insert to cassandra
 		statement = "INSERT INTO % (stock_symbol, trade_time, trade_price) VALUES ('%s','%s',%f)" % (data_tablem, symbol, tradetime, price)
 		cassandra_session.execute(statement)
 		logger.debug('finished save data for symbol: %s, price: %f, tradetime: %s' % (symbol, price, tradetime))

 	except Exception:
 		logger.error('Failed to save data to cassandra %s', stock_data)



if __name__ == '__main__':
 	parser = argparse.ArgumentParser()
 	parser.add_argument('topic_name', help='the kafka topic to read from')
 	parser.add_argument('kafka_broker', help='the ip address of kafka broker')
 	parser.add_argument('cassandra_broker', help='the ip of cassandra')
 	parser.add_argument('keyspace', help='the keyspace to use in cassandra')
 	parser.add_argument('data_table', help='the table to use')

 	# - parse arguments
 	args = parser.parse_args()
 	topic_name = args.topic_name
 	kafka_broker = args.kafka_broker
 	cassandra_broker = args.cassandra_broker
 	keyspace = args.keyspace
 	data_table = args.data_table

 	# - setup kafka consumer
 	consumer = KafkaConsumer(
 			topic_name,
 			bootstrap_servers=kafka_broker
 		)

 	# - setup cassandra connection
 	cassandra_cluster = Cluster(
			contact_points=cassandra_broker.split(',')
 		)

 	session = cassandra_cluster.connect()

	# - cql
 	session.execute("CREATE KEYSPACE IF NOT EXISTS %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'} AND durable_writes = 'true'" % keyspace)
 	session.set_keyspace(keyspace)
 	session.execute("CREATE TABLE IF NOT EXISTS %s (stock_symbol text, trade_time timestamp, trade_price float, PRIMARY KEY (stock_symbol, trade_time))" % data_table)

 	for msg in consumer:
 		persist_data(msg.value, session)
