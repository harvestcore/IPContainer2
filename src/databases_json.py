import json

users = []
data = []

class Data():
    def createNetwork(_username, _type):
        ret = False
        with open('./src/json/row_data.json') as f:
            data_json = json.load(f)
            data_json["username"] = _username
            data_json["type"] = _type
            data.append(data_json)
            ret = True

        return ret

    def addIPtoNetwork(_username, _type, _data):
        ret = False
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                x["data"].append(_data)
                ret = True

        return ret

    def updateData(_username, _type, _data):
        ret = True
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                x["data"] = _data
                ret = True

        return ret

    def delete(_username, _type):
        ret = False
        for i in range(len(data)):
            if data[i]["username"] == _username and data[i]["type"] == _type:
                data.pop(i)
                ret = True

        return ret

    def exist(_username, _type):
        ret = False
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                ret = True
        
        return ret

    def getData(_username, _type):
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                if isinstance(x["data"], list):
                    return x["data"]

    def tableSize():
        return len(data)

    def _dropTable():
        data.clear()

    def showData():
        return data


class Users():
    def insert(_username):
        users.append(_username)

    def delete(_username):
        users.remove(_username)

    def exist(_username):
        if _username in users:
            return True
        else:
            return False

    def tableSize():
        return len(users)

    def _dropTable():
        users.clear()

    def showUsers():
        return users