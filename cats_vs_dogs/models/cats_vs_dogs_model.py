from typing import Callable, Dict, Optional, Tuple
import numpy as np

from cats_vs_dogs.models.base import Model
#from cats_vs_dogs.datasets.emnist_dataset import EmnistDataset
from cats_vs_dogs.networks.mobile_net_v2 import mobile_net_v2
from cats_vs_dogs.utils import load_img

CATS_VS_DOGS_PRETRAINED_MODEL = '../weights/cats-vs-dogs-mobilenetv2.hdf5'
LABEL_NAME_MAP = {0: 'Cat', 1: 'Dog'}


class CatsVsDogsModel(Model):
    def __init__(self,
                 pretrained_model_uri = CATS_VS_DOGS_PRETRAINED_MODEL):
        """Define the default dataset and network values for this model."""
        super().__init__(pretrained_model_path=pretrained_model_uri)

    def predict(self, image_filename: str) -> str:

        image = load_img(image_filename)
        predicted_class_id = self.network.predict(image)
        print(predicted_class_id)
        predicted_class_name = LABEL_NAME_MAP[np.round(predicted_class_id[0][0])]

        return predicted_class_name
