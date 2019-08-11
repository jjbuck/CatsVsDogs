# Cats Vs Dogs Web App

This is the back-end service that provides the core ML logic for my web application to predict
whether an image is a cat or a dog. It's a Dockerized Flask application that runs a
pre-trained Tensorflow model at inference time. The model is trained in a notebook in this
repository called "notebooks/cats_vs_dogs.ipynb". Specifically, this uses a MobileNetV2
model that was originally trained on ImageNet and is fine-tuned on a TensorFlow cats-and-dogs dataset.

It uses https://github.com/jjbuck/CatsVsDogsInfrastructure as a starting point, which is generated from a generic template I created (https://github.com/jjbuck/FargateServiceInfrastructure).

The front end of this web app is http://jonathanjbuck.com/cats-vs-dogs/index.html.

# Possibilities for Improvement

Because this was only a personal exercise, there's a lot of room for improvement here, including
but not limited to
* Using a production web server instead of the Flask dev server
* Infrastructure auto scaling
* A fancier front end design
* More user configuration of the back-end ML model
* ...PRs welcome!

# Credits
This web app is inspired by (and sometimes uses code snippets directly from) the following.
* Full Stack Deep Learning (https://fullstackdeeplearning.com)
* https://www.fast.ai
* https://aws.amazon.com/getting-started/projects/build-modern-app-fargate-lambda-dynamodb-python/
* https://github.com/ryanml/NotHotDog