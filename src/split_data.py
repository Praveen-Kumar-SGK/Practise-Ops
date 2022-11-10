import pandas as pd

from get_data import read_params
import argparse
from sklearn.model_selection import train_test_split

def split_data(config_path):
    config=read_params(config_path)
    test_size=config['split_data']['test_size']
    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    random_state=config['base']['random_state']
    path=config['load_data']['raw_dataset_csv']
    df=pd.read_csv(path,sep=',')
    train,test=train_test_split(df,test_size=test_size,random_state=random_state)
    train.to_csv(train_path,sep=",", index=False, encoding="utf-8")
    test.to_csv(test_path,sep=",",index=False,encoding='utf-8')

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed=args.parse_args()
    split_data(parsed.config)