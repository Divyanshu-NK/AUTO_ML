from flask import Flask,request,jsonify
import pandas as pd
import os

app=Flask(__name__)

UPLOAD_FOLDER="uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER


@app.route("/",methods=['GET'])
def home():
    return jsonify({'message':'welcome to auto ml'})

@app.route("/uploads",methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"errro":"no files part"}),400
    
    file=request.files['files']
    
    if file.filename=="":
        return jsonify({'errro':"No selected files"}),400
    
    filepath=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
    
    file.save(filepath)
    
    return jsonify ({"message":"File upload successfull","filepath":filepath})       


if __name__=="__main__":
    app.run(debug=True)