from builtins import type
import logging

from typing import Callable, Dict, Optional
import numpy as np
from tensorflow.keras.models import Model as KerasModel
import tensorflow as tf

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Model:

    def __init__(self,
                 pretrained_model_path: str):
        self.network = self.load_model(pretrained_model_path)
        self.name = f'{self.__class__.__name__}_{self.network.name}'
        self.input_shape = self.network.get_layer(index=0).input.shape[1:3]

        self.network.summary()

    @property
    def image_shape(self):
        return self.input_shape

    def fit(self, dataset):
        pass

    def evaluate(self, X, y):
        preds = self.network.predict(X)
        return np.mean(np.argmax(preds, -1) == np.argmax(y, -1))

    def load_weights(self):
        pass

    @staticmethod
    def load_model(model_artifact_uri):
        logger.info(f'Attempting to load model from uri {model_artifact_uri}')
        try:
            model = tf.keras.models.load_model(model_artifact_uri)
            logger.info(f'Successfully loaded model from uri {model_artifact_uri}')
            return model
        except Exception as ex:
            logger.error(f'Unable to load model from {model_artifact_uri}')
            logger.error(ex)
            raise ex


