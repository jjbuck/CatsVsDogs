import boto3
import datetime as dt
import os
from moto import mock_cloudwatch


NAMESPACE = 'CatsVsDogs'
AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION", "us-west-2")



class CloudwatchClient:

    def __init__(self):
        if True:
            mock = mock_cloudwatch()
            mock.start()
            self.client = boto3.client('cloudwatch', region_name=AWS_DEFAULT_REGION)


    def put_predict_error_metric(self):
        metric_name = 'PredictFailed'
        #timestamp = dt.datetime.timestamp(dt.datetime.now())
        value = 1
        unit = 'Count'
        put_metric_data_request = {
            'Namespace': NAMESPACE,
            'MetricData' : [
                {
                    'MetricName': metric_name,
                    'Value': value,
                    'Unit': unit
                }
            ]
        }

        self.client.put_metric_data(**put_metric_data_request)


    def put_received_predict_request_metric(self):
        metric_name = 'PredictRequestReceived'
        #timestamp = dt.datetime.timestamp(dt.datetime.now())
        value = 1
        unit = 'Count'
        put_metric_data_request = {
            'Namespace': NAMESPACE,
            'MetricData' : [
                {
                    'MetricName': metric_name,
                    'Value': value,
                    'Unit': unit
                }
            ]
        }

        self.client.put_metric_data(**put_metric_data_request)
