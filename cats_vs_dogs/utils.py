from tensorflow.keras.preprocessing import image as image_utils
from tensorflow.python.keras.applications.imagenet_utils import preprocess_input
from PIL import Image

import numpy as np


IMG_SIZE = 160 # All images will be resized to 160x160


def load_img(image_filename: str) -> np.ndarray:
    image = image_utils.load_img(image_filename, target_size=(IMG_SIZE, IMG_SIZE))
    image = preprocess_input(image_utils.img_to_array(image), mode='tf')
    return np.expand_dims(image, axis=0)


