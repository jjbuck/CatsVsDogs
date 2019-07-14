import numpy as np
from typing import Tuple, Union
from ml_core.models import CatsVsDogsModel



class Predictor:

    def __init__(self, dataset_cls=IrisDataset):
        self.model = SVC(dataset_cls=dataset_cls)
        self.model.load_weights()

    def predict(self, features: np.ndarray) -> np.ndarray:
        if features.shape[1] % 4 != 0:
            raise Exception(f"Invalid input dimensions of shape {features.shape}")
        return self.model.predict(features)



class CharacterPredictor:
    """Given an image of a single handwritten character, recognizes it."""
    def __init__(self):
        self.model = CharacterModel()
        self.model.load_weights()

    def predict(self, image_or_filename: Union[np.ndarray, str]) -> Tuple[str, float]:
        """Predict on a single image."""
        if isinstance(image_or_filename, str):
            image = util.read_image(image_or_filename, grayscale=True)
        else:
            image = image_or_filename
        return self.model.predict_on_image(image)

    def evaluate(self, dataset):
        """Evaluate on a dataset."""
        return self.model.evaluate(dataset.x_test, dataset.y_test)