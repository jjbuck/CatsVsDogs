from tensorflow.keras.preprocessing import image as image_utils
from tensorflow.python.keras.applications.imagenet_utils import preprocess_input
from PIL import Image
import urllib.request
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

IMG_SIZE = 160 # All images will be resized to 160x160


def load_image_from_file_or_url(image_filename_or_url: str) -> np.ndarray:
    logger.info(f'Received request to load image or filename {image_filename_or_url}.')
    if is_url(image_filename_or_url):
        logger.info('Loading from uri.')
        image = load_image_from_url(image_filename_or_url)
    else:
        logger.info('Loading from image file.')
        image = load_local_img_file(image_filename_or_url)
    image = preprocess_input(image_utils.img_to_array(image), mode='tf')
    return np.expand_dims(image, axis=0)


def is_url(string: str) -> bool:
    return True if string[:4] == 'http' else False


def load_local_img_file(image_filename: str) -> np.ndarray:
    logger.info(f'Attempting to open image {image_filename}')
    image = image_utils.load_img(image_filename, target_size=(IMG_SIZE, IMG_SIZE))
    return image


def load_image_from_url(url: str) -> Image:
    logger.info(f'Fetching url {url}')
    image = Image.open(urllib.request.urlopen(url))
    image = resize_pil_image(image, target_size=(IMG_SIZE, IMG_SIZE))
    return image

# https://github.com/keras-team/keras-preprocessing/blob/master/keras_preprocessing/image/utils.py
def resize_pil_image(pil_image: Image, target_size):
    width_height_tuple = (target_size[1], target_size[0])
    resample = Image.NEAREST
    img = pil_image.resize(width_height_tuple, resample)
    return img