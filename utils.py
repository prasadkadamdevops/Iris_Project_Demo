import config
import pickle
import json
import numpy as np
import pandas as pd
import os

class Iris():
    def __init__(self, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_model(self):

        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.json_data = json.load(f)

    def get_predict_species(self):
        self.load_model()

        # Create test_array with the required features
        test_array = np.array([self.SepalLengthCm, self.SepalWidthCm, self.PetalLengthCm, self.PetalWidthCm])

        # Create DataFrame for prediction with the correct feature names
        feature_names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        test_array_df = pd.DataFrame([test_array], columns=feature_names)

        # Make prediction using the DataFrame
        predicted_spec = self.model.predict(test_array_df)

        # Mapping predictions to species
        species_mapping = {0: "setosa", 1: "versicolor", 2: "virginica"}
        predicted_species = species_mapping.get(predicted_spec[0], "Unknown")

        return predicted_species



if __name__ == '__main__':
    print("Current Working Directory:", os.getcwd())

    SepalLengthCm = 30.0
    SepalWidthCm = 23
    PetalLengthCm = 28.3
    PetalWidthCm = 2

    ir = Iris(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    print(ir.get_predict_species())
