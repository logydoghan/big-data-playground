# big-data-playground
Straightforward implementation of various big data frameworks


Kafka - Stock Price Fetcher
python data-producer.py GOOG(or other stock tickers) 192.168.99.101:9092 (Docker env ip address : kafka port) stock-analyzer

Cassandra - Stock Price Storage
python data-storage.py stock-analyzer 192.168.99.100:9092 192.168.99.100 stock stock (new keyspace)

