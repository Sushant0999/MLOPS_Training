import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TEST_FILE = 'house_price_test.csv'

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = ''