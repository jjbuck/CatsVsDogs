from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import logging
import sys, os
#sys.path.append(
#    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append("..")

from cats_vs_dogs.models import CatsVsDogsModel


app = Flask(__name__)
CORS(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
@app.route('/')
def hello_world():
    return jsonify({"message" : "Hello world!"})

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    logger.info(f'Received request {request}')
    logger.info(request.__dict__)
    logger.info(f'Form: {request.form}')
    logger.info(f'Files: {request.files}')

    if request.form:
        logger.info('Received form data.')
        image_filename = request.form.get('url')
        logger.info(f'Data: {image_filename}')
    elif request.files:
        logger.info('Received file data.')
        image_filename = request.files.get('file', None)
        logger.info(f'Data: {image_filename}')
    else:
        logger.info('Received unknown data type.')
        return jsonify({'message': 'Unknown input type. Prediction will not be returned.'})

    model = CatsVsDogsModel()
    pred = model.predict(image_filename)

    return jsonify({"message" : f'{pred}',
                    "form": f'{request.form}',
                    "file": f'{request.files}',
                    "args": f'{request.args}'})


# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

