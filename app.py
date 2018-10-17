import json
from flask import Flask, jsonify
from src.ipcontainer import IPContainer

app = Flask(__name__)

@app.route("/")
def hello():
    return "who dis"

@app.route("/addUser/<user>")
def addUser(user):
    return jsonify(success=IPContainer.addUser(str(user)))

@app.route("/removeUser/<user>")
def removeUser(user):
    return jsonify(success=IPContainer.removeUser(str(user)))

@app.route("/getNumberOfUsers", methods=['GET'])
def getNumberOfUsers():
    return jsonify(users=IPContainer.getNumberOfUsers())

@app.route("/getNumberOfNetworks", methods=['GET'])
def getNumberOfNetworks():
    return jsonify(networks=IPContainer.getNumberOfNetworks())

@app.route("/existNetwork/<user>/<_type>")
def existNetwork(user, _type):
    return jsonify(exists=IPContainer.existNetwork(str(user), str(_type)))

@app.route("/createNetwork/<user>/<_type>")
def createNetwork(user, _type):
    return jsonify(success=IPContainer.createNetwork(str(user), str(_type)))

@app.route("/removeNetwork/<user>/<_type>")
def removeNetwork(user, _type):
    return jsonify(success=IPContainer.removeNetwork(str(user), str(_type)))

@app.route("/addIPtoNetwork/<user>/<_type>/<ip>")
def addIPtoNetwork(user, _type, ip):
    return jsonify(success=IPContainer.addIPtoNetwork(str(user), str(_type), str(ip)))
    
@app.route("/removeIPfromNetwork/<user>/<_type>/<ip>")
def removeIPfromNetwork(user, _type, ip):
    return jsonify(success=IPContainer.removeIPfromNetwork(str(user), str(_type), str(ip)))

@app.route("/getNetworkSize/<user>/<_type>")
def getNetworkSize(user, _type):
    return jsonify(user=user, network=_type, size=IPContainer.getNetworkSize(str(user), str(_type)))

@app.route("/getData/<user>/<_type>")
def getData(user, _type):
    return jsonify(user=user, network=_type, data=IPContainer.getData(str(user), str(_type)))

@app.route("/_dropUsers")
def _dropUsers():
    IPContainer._dropUsers()

@app.route("/_dropData")
def _dropData():
    IPContainer._dropData()

@app.route("/getUsers")
def getUsers():
    return jsonify(users=IPContainer.getUsers())

if __name__ == "__main__":
    app.run()