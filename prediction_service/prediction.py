import os
import yaml
import json
import numpy as np
import joblib

params_path='params.yaml'
schema_path = os.path.join('prediction_service','schema.json')
class NotInRange(Exception):
    def __init__(self,message='Values entered are not in expected range'):
        self.message = message
        super().__init__(self.message)

class NotInCols(Exception):
    def __init__(self,message='Not in Columns'):
        self.message =message
        super().__init__(self.message)

def read_params(config_path=params_path):
    with open(config_path) as f:
        config=yaml.safe_load(f)
    return config

def predict(data):
    config=read_params(params_path)
    model_dir=config['model_dir']
    model=joblib.load(model_dir)
    prediction=model.predict(data).tolist()[0]
    try:
        if 3 <= prediction <=8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"

def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_request):
    def validate_cols(col):
        schema = get_schema()
        actual_col= schema.keys()
        if col not in actual_col:
            raise NotInCols

    def validate_values(col,val):
        schema=get_schema()
        if not(schema[col]['min']<=float(dict_request[col])<=schema[col]['max']) :
            raise NotInRange

    for col,val in dict_request.items():
        validate_cols(col)
        validate_values(col,val)
    return True

def form_response(dict_request):
    if validate_input(dict_request):
        data = dict_request.values()
        data = [list(map(float,data))]
        response = predict(data)
        return response
    else:
        return "Please check the data"

def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data= np.array([dict_request.values()])
            response = predict(data)
            response= {'response':response}
            return response
    except NotInRange as e:
        response = {'Expected values in Range': json.load(schema_path),'response':str(e)}
    except NotInCols as e:
        response = {"Expected Col":json.load(schema_path),'response':str(e)}
    except Exception as e:
        response={'Error':str(e)}
