import boto3
import datetime as dt


NAMESPACE = 'CatsVsDogs'

class CloudwatchClient:

    def __init__(self):
        self.client = boto3.client('cloudwatch')


    def put_request_received_metric(self):
        metric_name = 'RequestReceived'
        timestamp = dt.datetime.time()
        value = 1
        unit = 'Seconds'
        put_metric_data_request = {
            'Namespace': NAMESPACE,
            'MetricData' : [
                {
                    'MetricName': metric_name,
                    'Timestamp': timestamp,
                    'Value': value,
                    'Unit': unit
                }
            ]
        }

        self.client.put_metric_data(**put_metric_data_request)
