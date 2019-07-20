#!/usr/bin/env bash

export AWS_ACCOUNT_ID="784757526031"
export APP_NAME="CatsVsDogs"
docker build . -t ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME_LOWERCASE}:latest

docker run -d -p 8080:8080 ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME_LOWERCASE}:latest
# http://localhost:8080
# curl http://127.0.0.1:8080/predict?image_url=https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg
# curl -X POST -F "url=https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg" http://127.0.0.1:8080/predict
# curl -X POST -F "file=@../cats_vs_dogs/tests/resources/Golden_Retriever_Carlos_(10581910556).jpg" http://127.0.0.1:8080/predict
# docker stop $(docker ps -aq)
