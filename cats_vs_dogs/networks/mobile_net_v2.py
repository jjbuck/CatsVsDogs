"""CNN-based model recognizing images"""
from typing import Tuple

import tensorflow as tf
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
from tensorflow.keras.models import Model as KerasModel


def mobile_net_v2(input_shape):

    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape,
                                                   include_top=False,
                                                   weights='imagenet')

    global_average_layer = tf.keras.layers.GlobalAveragePooling2D()

    prediction_layer = keras.layers.Dense(1, activation='sigmoid')

    for layer in base_model.layers:
        layer.trainable = False

    model = tf.keras.Sequential([
        base_model,
        global_average_layer,
        prediction_layer
    ])

    return model

