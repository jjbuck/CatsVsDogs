import boto3
import datetime as dt


NAMESPACE = 'CatsVsDogs'

class CloudwatchClient:

    def __init__(self):
        self.client = boto3.client('cloudwatch')


    def put_request_received_metric(self):
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
