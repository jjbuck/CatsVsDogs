from cats_vs_dogs.utils import load_image_from_file_or_url
import pytest

TEST_IMAGE_URL = 'https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg'

def test_load_image_from_file_or_url():
    image = load_image_from_file_or_url(TEST_IMAGE_URL)
    assert image.shape == (1, 160, 160, 3)