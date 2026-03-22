#!/bin/bash

CONTAINER_NAME=customer_pipeline
mkdir -p customer-analytics/results

for file in *.csv *.txt *.png; do
  docker cp $CONTAINER_NAME:/app/pipeline/$file customer-analytics/results/
done

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME