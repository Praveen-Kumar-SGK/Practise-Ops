# Load data from the got data and replacing the columns names

from get_data import get_data,read_params
import argparse

def load_and_save(config_path):
    config=read_params(config_path)
    df=get_data(config_path)
    df=df.iloc[:,1:]
    new_col= [i.replace(" ","_") for i in df.columns]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",",header=new_col)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument('--config',default= 'params.yaml')
    parsed=args.parse_args()
    load_and_save(parsed.config)
