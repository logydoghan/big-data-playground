# Docker Script

## 

1. local-setup.sh to setup Kakfa, Cassandra, Zookeeper environment

## MacOS, *nix

1. create docker-machine with 2 CPU and 2G memory
```sh
docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory 2048 bigdata
```
2. run to start Kafka, Cassandra, Zookeeper
```sh
./local-setup.sh bigdata
```
