
import json
import os.path
import requests


#from api.v1 import api_v1 
from flask import Flask
from flask import render_template, jsonify, request, Blueprint
from v1.api import order


#Set app flask
app = Flask(__name__)

#Set api url prefix
#app.register_blueprint(api_v1, url_prefix='/api/v1')

#Set flask config
#Jsonify ASCII 설정 -> False : 한글 깨짐 방지
#app.co


@app.route("/", methods=["GET", "POST"])
def index():
    #name = request.form.get('홍길동')
    names = '홍길동'
    idx = '이상목'
    return render_template("index.html",name = names,
    id = idx)


@app.route("/action", methods=["GET", "POST"])
def aa(): 
    return(order.pp())



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
#app.run(debug=True, port=5050)

