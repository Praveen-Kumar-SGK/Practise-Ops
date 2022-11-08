#### 1.Steps to Initialize Git Repository
```
git clone https://github.com/Praveen-Kumar-SGK/simple-dvc-demo.git
```
```
git init
```
#### 2.DVC
```
dvc init
```
#### 3.Create requirements.txt
 ```
pip install -r requirements.txt
```
#### 4.Create template.py 
- It creates empty folders - data(raw,processed), notebooks, src, templates, saved_models etc
- It creates empty files - (src,__init__.py), dvc.yaml, params.yaml , .gitignore
#### Uplaoding the created files
```
git add .
```
```
git commit -m "First Commit"
```
```
git push origin main
```
If you want single line command for git
```
git add . && git commit -m "First Commit" && git push origin main
```