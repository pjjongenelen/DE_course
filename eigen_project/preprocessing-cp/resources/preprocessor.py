# MLP for Pima Indians Dataset saved to single file
# see https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import json
import os

from sklearn import model_selection, preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error




def clean(dataset):
    # split into input (X) and output (Y) variables
    # Y = dataset.iloc[:,2].tolist()
    dataset = dataset.drop(columns=["Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D", "Contract_Valid_Until"], axis=1)


    text_out = {
        "Preprocessing done": "successful"
    }
    # Saving model in a given location (provided as an env. variable
    data_repo = os.environ['DATA_REPO']
    if data_repo:
        file_path = os.path.join(data_repo, "preprocessed_data.json")
        dataset.to_json(file_path)
    else:
        dataset.to_json("preprocessed_data.json")
        return json.dumps({'message': 'The data was saved locally.'},
                          sort_keys=False, indent=4), 200

    print("Saved the data to disk")
    return json.dumps(text_out, sort_keys=False, indent=4)
