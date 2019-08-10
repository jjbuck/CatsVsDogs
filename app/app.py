from flask import Flask, jsonify, json, Response, request, abort, make_response
from flask_cors import CORS
import logging
import sys, os
#sys.path.append(
#    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append("..")

from cats_vs_dogs.models import CatsVsDogsModel
from cats_vs_dogs.clients import cloudwatch_client


app = Flask(__name__)
CORS(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
@app.route('/')
def hello_world():
    return jsonify({"message" : "Hello world!"})

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    cloudwatch_client.put_received_predict_request_metric()

    logger.info(f'Received request {request}')
    logger.info(request.__dict__)
    logger.info(f'Form: {request.form}')
    logger.info(f'Files: {request.files}')
    logger.info(f'JSON: {request.json}')


    if request.form:
        logger.info('Received form data.')
        image_filename = request.form.get('url')
        logger.info(f'Data: {image_filename}')
    elif request.files:
        logger.info('Received file data.')
        image_filename = request.files.get('file', None)
        logger.info(f'Data: {image_filename}')
    else:
        logger.info('Unknown input type.')
        abort(400, 'Unknown input type. Please check inputs and try again.')

    try:
        model = CatsVsDogsModel()
        pred = model.predict(image_filename)
    except Exception as ex:
        cloudwatch_client.put_predict_error_metric()
        logger.error('Encountered internal server error.')
        logger.error(ex)
        abort(500, 'Internal server error. Please try again later.')

    return jsonify({"message": f'{pred}'})


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': '400 Bad Request'}), 400)

# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

