from typing import Callable, Dict, Optional, Tuple
import numpy as np
import logging
import sys

from cats_vs_dogs.models.base import Model
from cats_vs_dogs.utils import load_image_from_file_or_url

CATS_VS_DOGS_PRETRAINED_MODEL = 'cats_vs_dogs/weights/cats-vs-dogs-mobilenetv2.hdf5'
LABEL_NAME_MAP = {0: 'Cat', 1: 'Dog'}

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

class CatsVsDogsModel(Model):
    def __init__(self,
                 pretrained_model_uri = CATS_VS_DOGS_PRETRAINED_MODEL):
        """Define the default dataset and network values for this model."""
        super().__init__(pretrained_model_path=pretrained_model_uri)

    def predict(self, image_filename: str) -> str:

        image = load_image_from_file_or_url(image_filename)
        prediction = self.network.predict(image)
        logger.info(f'Prediction: {prediction}')
        predicted_class_name = LABEL_NAME_MAP[np.round(prediction[0][0])]
        logger.info(f'Predicted class: {predicted_class_name}')

        return predicted_class_name
