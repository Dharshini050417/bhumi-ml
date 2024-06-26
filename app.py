from flask import Flask,jsonify
from usersPredict import usersPredict 

app=Flask(__name__)

data=usersPredict()

@app.route("/get-users",methods=['GET'])
def getusers():
    return jsonify(data)

if (__name__=='__main__'):
    app.run(debug=True)