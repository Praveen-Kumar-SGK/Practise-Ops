import os
import json
import joblib
import argparse
import numpy as np
import pandas as pd

from get_data import read_params
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
def metrics(actual,pred):
    rmse=np.sqrt(mean_squared_error(actual,pred))
    mae=mean_absolute_error(actual,pred)
    r2=r2_score(actual,pred)
    return rmse,mae,r2

def train_evaluate(config_path):
    config=read_params(config_path)
    train=pd.read_csv(config['split_data']['train_path'],sep=',')
    test=pd.read_csv(config['split_data']['test_path'],sep=',')
    train_x=train.drop([config['base']['target_col']],axis=1)
    train_y=train[config['base']['target_col']]
    test_x=test.drop([config['base']['target_col']],axis=1)
    test_y=test[[config['base']['target_col']]]
    # model=config['estimators']['ElasticNet']
    l1_ratio=config['estimators']['ElasticNet']['params']['l1_ratio']
    alpha=config['estimators']['ElasticNet']['params']['alpha']
    lr=ElasticNet(l1_ratio=l1_ratio , alpha=alpha)
    lr.fit(train_x,train_y)
    pred=lr.predict(test_x)
    rmse, mae, r2=metrics(test_y,pred)
    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)
#----------------------------------------------------------------------------------------------
    params_path=config['reports']['params']
    scores_path=config['reports']['scores']

    with open(params_path,'w') as p:
        parameters={"l1_ratio":l1_ratio,"alpha":alpha}
        json.dump(parameters,p,indent=2)

    with open(scores_path,'w') as s:
        scores = {"RMSE":rmse,"MAE":mae,"R2":r2}
        json.dump(scores,s,indent=2)
#----------------------------------------------------------------------------------------------
    model_path=os.path.join(config['model_dir'],"ElasticNet.joblib")
    joblib.dump(lr,model_path)



if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed=args.parse_args()
    train_evaluate(parsed.config)