from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import logging

import sys
sys.path.append("..") # Adds higher directory to python modules path.


app = Flask(__name__)
CORS(app)

logger = logging.getLogger(__name__)

# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
@app.route('/')
def hello_world():
    return jsonify({"message" : "Hello world!"})

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.form:
        logger.info('Received form data.')
        logger.info(f'Data type: {type(request.form)}')
        url = request.form.get('url')
    elif request.files:
        logger.info('Received file data.')
        logger.info(f'Data type: {type(request.files)}')
        file = request.files.get('file', None)
    else:
        logger.info('Received unknown data type.')

    return jsonify({"message" : "Hello from /predict!",
                    "form": f'{request.form}',
                    "file": f'{request.files}',
                    "args": f'{request.args}'})


# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

