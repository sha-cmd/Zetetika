import sys
from .ModelVariables import ModelVariables
from tools import data_simple_treatment
from tools import data_augmented
from tools import BATCH_SIZE

class DataGenerator(ModelVariables):
    def __init__(self, batch_size=BATCH_SIZE):
        super().__init__()
        print('Eager loading ready')
        self.size_batch = batch_size

    def __call__(self, path_images, path_masks, data_mix='NA'):
        if data_mix == "original_version":
            return self.data_vo()
        elif data_mix == "augmented":
            return self.data_aug()
        elif data_mix == "multiplication":
            return self.data_multiplication()
        else:
            print('paramètre data_mix vaut "augmented", "multiplication" ou "original_version"')
            sys.exit()

    def data_vo(self):
        print('data_vo')
        return data_simple_treatment(self.path_images, self.path_masks, self.size_batch)

    def data_aug(self):
        print('data_aug')
        return data_augmented(self.path_images, self.path_masks, self.size_batch)

    def data_multiplication(self):
        print('data_multiplication')
        return data_simple_treatment(self.path_images, self.path_masks, self.size_batch)
