import os

# os.path.join - creates sub folders
directories = [os.path.join('data','raw'),
               os.path.join('data','processed'),
               'data_given',
               'src',
               'templates',
               'notebooks',
               'saved_models']

for directory in directories:
    os.makedirs(directory,exist_ok=True)
    with open(os.path.join(directory,'.gitkeep'),'w') as f:
        pass

# Files needed to be created
files=['dvc.yaml',
       'params.yaml',
       '.gitignore',
       os.path.join('src','__init__.py'),
       os.path.join('src','get_data.py'),
       os.path.join('src','load_data.py'),
       os.path.join('src','split_data.py'),
       os.path.join('src','train_and_evaluate.py')]

for file in files:
    with open(file,'w') as f:
        pass