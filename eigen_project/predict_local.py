import json
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from flask import Flask
server_port = 5000
app = Flask(__name__)
@app.route('/')
# This is a local implementation of our model_trainer file in the training component
# The code is very similar, but not identical. Please keep in mind:
# - we don't save the trained model
# - we call the function using some operations from the json and pandas packages
# - it uses mc_data.json instead of data_for_model_creation.json


def train():
    dataset = pd.DataFrame.from_dict(json.load(open("mc_data.json")))
    # split into input (X) and output (Y) variables
    # Y = dataset.iloc[:, 2].tolist()
    # X = dataset.drop(columns=['Value', "Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D", "Contract_Valid_Until"], axis=1)

    model = xgb.XGBRegressor()
    model.load_model('trained_model.json')
    val_set2 = dataset.copy()
    dataset = dataset.drop(columns=["Value", "Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D",
                                    "Contract_Valid_Until"], axis=1)
    # hier nog string values etc weggooien
    result = model.predict(dataset)
    y_classes = result.argmax(axis=-1)
    val_set2['Value'] = y_classes.tolist()
    dic = val_set2.to_dict(orient='records')
    # mse = mean_squared_error(y_test, y_pred)

    return 'yes'


    # We don't save the model in this instance

if __name__ == "__main__":
    app.run('0.0.0.0',port=server_port)