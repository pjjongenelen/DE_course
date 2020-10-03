import json
import os
import xgboost as xgb
#from keras.models import load_model
# make prediction
def predict(dataset):
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.json")
        model = xgb.XGBRegressor()
        model.load_model(file_path)
        val_set2 = dataset.copy()
        dataset = dataset.drop(columns=["Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D", "Contract_Valid_Until"], axis=1)
        #hier nog string values etc weggooien
        result = model.predict(dataset)
        y_classes = result.argmax(axis=-1)
        val_set2['Value'] = y_classes.tolist()
        dic = val_set2.to_dict(orient='records')
        return json.dumps(dic, indent=4, sort_keys=False)
    else:
        return json.dumps({'message': 'A model cannot be found.'},
                          sort_keys=False, indent=4)