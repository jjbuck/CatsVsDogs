import sys
import pytest
import json
sys.path.append("..")
from app import app
from flask import Flask, jsonify, json, Response, request, Request

TEST_EXPECTED_PREDICT_RESPONSE_NO_INPUT = "400 Bad Request"
TEST_IMAGE_URL = 'https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg'
TEST_EXPECTED_CLASS_NAME = 'Dog'

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def test_app_predict_no_input(client):
    response = client.post('/predict')
    assert TEST_EXPECTED_PREDICT_RESPONSE_NO_INPUT in json.loads(response.data)['error']


def test_app_predict_url_input(client):
    response = client.post('/predict', data={'url': TEST_IMAGE_URL})
    assert json.loads(response.data)['message'] == TEST_EXPECTED_CLASS_NAME


