# MLP for Pima Indians Dataset saved to single file
# see https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import json
import os
import xgboost as xgb
from sklearn import model_selection, preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error




def train(dataset):
    # split into input (X) and output (Y) variables
    df =
    Y = dataset['Value']
    X = dataset.drop('Value', axis=1)

    # make train_test split
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state = 42)
    # define model
    model = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.3, learning_rate=0.1,
                             max_depth=4, alpha=1, n_estimators=1)
    # Fit the model
    model.fit(x_train, y_train)
    # evaluate the model
    train_score = model.score(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)

    text_out = {
        "Training Score": train_score,
        "MSE": mse,
    }
    # Saving model in a given location (provided as an env. variable
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.h5")
        model.save(file_path)
    else:
        model.save("model.h5")
        return json.dumps({'message': 'The model was saved locally.'},
                          sort_keys=False, indent=4), 200

    print("Saved the model to disk")
    return json.dumps(text_out, sort_keys=False, indent=4)
