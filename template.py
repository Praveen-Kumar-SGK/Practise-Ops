import os

# os.path.join - creates sub folders
directories = [os.path.join('data','raw'),
               os.path.join('data','processed'),
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
       os.path.join('src','__init__.py')]

for file in files:
    with open(file,'w') as f:
        pass