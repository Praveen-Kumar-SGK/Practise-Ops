from flask import Flask,render_template,request,jsonify
import os
import numpy as np
from prediction_service import prediction

static_dir = os.path.join('webapp','static')
template_dir = os.path.join('webapp','templates')

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)


@app.route('/',methods=['GET','POST'])
def index():
    if request.methods=='POST':
        try:
            if request.form:
                dict_req=dict(request.form)
                response=prediction.form_response(dict_req)
                return render_template('index.html',response=response)
            elif request.json:
                response=prediction.api_response(request.json)
        except Exception as e:
            print(e)
            error = {"Error": e}
            return render_template('404.html',error=error)
    else:
        render_template("index.html")

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)