from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS

from cats_vs_dogs.predictor import Predictor

app = Flask(__name__)
CORS(app)

# The service basepath has a short response just to ensure that healthchecks
# sent to the service root will receive a healthy response.
@app.route('/')
def hello_world():
    return jsonify({"message" : "Hello world!"})

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return jsonify({"message" : "Hello from /predict!",
                    "form": f'{request.form}',
                    "file": f'{request.files}'})


# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

