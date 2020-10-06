import os
import pandas as pd
import requests
from flask import Flask, json, Response

from resources import model_trainer

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/training-cp/<model>', methods=['POST'])
def train_models(model):
    db_api = os.environ['TRAIN_DB_API']
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    if model == "fifa":
        js = model_trainer.train(df)
        resp = Response(js, status=200, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST'
        resp.headers['Access-Control-Max-Age'] = '1000'
        return resp
    else:
        return json.dumps({'message': 'the given model is not supported dropped'},
                          sort_keys=False, indent=4), 400

@app.route('/training-db/<table_name>', methods=['GET'])
def read_data(table_name):
    db_api = os.environ['TRAIN_DB_API']
    r = requests.get(db_api)
    resp = Response(r, status=200)

    #df = read_data_records(table_name)
    #df = df.drop(columns=['ID'])
    #resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')

app.run(host='0.0.0.0', port=5000)
