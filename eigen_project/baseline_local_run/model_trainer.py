import json
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# This is a local implementation of our model_trainer file in the training component
# The code is very similar, but not identical. Please keep in mind:
# - we don't save the trained model
# - we call the function using some operations from the json and pandas packages


def train(dataset):
    # split into input (X) and output (Y) variables
    Y = dataset.iloc[:, 2].tolist()
    X = dataset.drop(columns=['Value', "Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D", "Contract_Valid_Until"], axis=1)

    # make train_test split
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
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

    # We don't save the model in this instance

train(pd.DataFrame.from_dict(json.load(open("mc_data.json"))))

dataset = pd.DataFrame.from_dict(json.load(open("mc_data.json")))
print(dataset.columns)