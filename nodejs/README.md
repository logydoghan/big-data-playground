# Node.js

## index.js
Display website for stock warehouse

### Dependencies
socket.io       http://socket.io/

redis           https://www.npmjs.com/package/redis

smoothie        https://www.npmjs.com/package/smoothie

minimist        https://www.npmjs.com/package/minimist

```sh
npm install
```

### Run code
bigdata docker-machine assume ip: 192.168.99.100
```sh
node index.js --port=3000 --redis_host=192.168.99.100 --redis_port=6379 --subscribe_topic=average-stock-price
```
