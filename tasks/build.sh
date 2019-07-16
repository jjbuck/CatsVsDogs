#!/usr/bin/env bash

export AWS_ACCOUNT_ID="784757526031"
export APP_NAME="CatsVsDogs"
docker build . -t ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME_LOWERCASE}:latest

docker run -d -p 8080:8080 ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME_LOWERCASE}:latest
# http://localhost:8080