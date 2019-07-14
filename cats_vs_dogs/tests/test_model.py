import os
import pytest

from cats_vs_dogs.models.base import Model
from cats_vs_dogs.models import CatsVsDogsModel


TEST_MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'weights/cats-vs-dogs-mobilenetv2.hdf5'))
TEST_IMAGE_FILENAME_DOG = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources/Golden_Retriever_Carlos_(10581910556).jpg'))
TEST_EXPECTED_CLASS_NAME_FOR_DOG_IMAGE = 'Dog'


def test_cats_vs_dogs_model_init_pretrained_success():
    model = CatsVsDogsModel(TEST_MODEL_PATH)
    assert model is not None


def test_cats_vs_dogs_model_predict_success():
    model = CatsVsDogsModel(TEST_MODEL_PATH)
    pred = model.predict(TEST_IMAGE_FILENAME_DOG)
    assert pred == TEST_EXPECTED_CLASS_NAME_FOR_DOG_IMAGE
