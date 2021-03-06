#!/usr/bin/env bash

export AWS_ACCOUNT_ID="784757526031"
export APP_NAME="CatsVsDogs"
docker build . -t ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME_LOWERCASE}:latest

docker run -d -p 8080:8080 ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME_LOWERCASE}:latest

# http://localhost:8080

# Test url input
# curl -X POST -H "Content-Type: application/json" -d '{"url":"https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg"}' http://127.0.0.1:8080/predict

# Test file upload input
# curl -X POST -F "file=@./cats_vs_dogs/tests/resources/Golden_Retriever_Carlos_(10581910556).jpg" http://127.0.0.1:8080/predict

# Useful commands

# Stop all running containers
# docker stop $(docker ps -aq)

# List containers
# docker container ls
