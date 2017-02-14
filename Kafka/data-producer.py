# connect to any kafka broker
# fetch stock prices

import argparse
import logging
import kafka
import kafka.errors
import socket
import json
import googlefinance
import time
import schedule
import atexit



# logging configuration
logging.basicConfig()                       #doing basic configuration for logging system
logger=logging.getLogger("Stock_Fetcher")   #returning a reference to a logger object with the given name

logger.setLevel(logging.DEBUG)

symbol="AAPL"
kafka_broker="192.168.99.101:9092"
topic="Stock_Analyzer"


def fetch_price(producer, symbol):
    logger.debug("Start to fetch price of %s" % symbol)
    price=json.dumps(googlefinance.getQuotes(symbol))
    producer.send(topic=topic, value=price, timestamp_ms=time.time())
    logger.debug("Finishing sending price of %s and the price is %s" % (symbol, price))


def shut_down(producer):
    logger.debug("Exiting program")
    producer.flush(10)
    producer.close()
    logger.debug("Producer is closed. Exiting.")




if __name__=="__main__":
    # setup commandline arguments
    parser=argparse.ArgumentParser()

    parser.add_argument("symbol", help="Stock Name")
    parser.add_argument("kafka_broker", help="Location of Kafka Broker")
    parser.add_argument("topic", help="the topic to use")

    args=parser.parse_args()             #args is of type Namespace defined in argparse module
    symbol=args.symbol
    topic=args.topic
    kafka_broker=args.kafka_broker

    #logger.debug("The stock name is %s" % symbol)

    #instantiate a kafka producer
    producer=kafka.KafkaProducer(bootstrap_servers=kafka_broker)

    #producer.send(topic=topic, value="Hello World")

    #fetch_price(producer, "AAPL")

    schedule.every(1).second.do(fetch_price, producer, symbol)

    atexit.register(shut_down, producer)

    while True:                          #capitalized first letter
        schedule.run_pending()
        time.sleep(1)
