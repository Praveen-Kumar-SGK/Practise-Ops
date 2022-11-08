#### 1. Steps to Initialize Git Repository
```
git init
```
```
git clone https://github.com/Praveen-Kumar-SGK/simple-dvc-demo.git
```
#####Or if you want to push it to the repo by command line
```
git remote add origin  https://github.com/Praveen-Kumar-SGK/simple-dvc-demo.git
```
#### 2. DVC
```
dvc init
```
#### 3. Create requirements.txt
 ```
pip install -r requirements.txt
```
#### 4. Create template.py 
- It creates empty folders - data(raw,processed), notebooks, src, templates, saved_models etc
- It creates empty files - src(__init__.py,get_data,load,split,evaluate), dvc.yaml, params.yaml , .gitignore
#### 5. Uploading the created files
```
git add .
```
```
git commit -m "First Commit"
```
```
git push origin main
```
- If you want single line command for git
```
git add . && git commit -m "First Commit" && git push origin main
```
#### 6. Download dataset and placing in data_given folder
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

#### 7. Adding files to DVC
- Github does not hold bigger files but dvc will save it in our google drive and track the version.
```
dvc add data_given/winequality.csv
```
#### 8. Source files 
- get_data : 
- load_data :
- split_data :
- train_and_evaluate :