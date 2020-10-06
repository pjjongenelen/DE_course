import os
import pandas as pd
import requests
from flask import Flask, json, Response, request

from resources import preprocessor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/preprocessing-cp/<model>', methods=['POST'])
def preprocessing_models(model):
    db_api = os.environ['TRAIN_DB_API']
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    if model == "fifa":
        js = preprocessor.clean(df)
        resp = Response(js, status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST'
        resp.headers['Access-Control-Max-Age'] = '1000'
        return request.get_json()
    else:
        return json.dumps({'message': 'the given model is not supported dropped'},
                          sort_keys=False, indent=4), 400




# To be deleted
data_repo = os.environ['DATA_REPO']
file_path_data = os.path.join(data_repo + "/preprocessed_data.json")

# For debugging, no actual fucntionality
@app.route('/preprocessing-cp/<table_name>', methods=['GET'])
def read_data(table_name):
    resp = Response(file_path_data, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST'
    resp.headers['Access-Control-Max-Age'] = '1000'
    preprocessed_data_test = resp.json

       # pd.read_json(resp)
    return preprocessed_data_test
# End to be deleted








app.run(host='0.0.0.0', port=5000)
