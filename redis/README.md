# Redis

## redis-producer.py
Redis producer fetch info from Kafka topic and then publish to redis PUB

### Dependencies
kafka-python    https://github.com/dpkp/kafka-python

redis           https://pypi.python.org/pypi/redis

```sh
pip install -r requirements.txt
```

### Run code
Assume docker machine ip: 192.168.99.100
```sh
python redis-publisher.py average-stock-price 192.168.99.100:9092 average-stock-price 192.168.99.100 6379
```


