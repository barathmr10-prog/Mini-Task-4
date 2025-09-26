from flask import Flask, jsonify, request

 
app = Flask(__name__)

users = dict()
user_pk = 1

@app.route('/',methods = ['GET','POST'])
def CreateView_users():
    if request.method == 'GET':
        return jsonify(list(users.values())),200

    elif request.method == 'POST':
        global user_pk
        pk_id = user_pk
        detail = request.json
        users[user_pk] = {
            'name' : detail.get('name'),
            'age' : detail.get('age'),
            'designation' : detail.get('designation'),
            'skill' : detail.get('skill')
        }
        user_pk +=1
        return jsonify(users[pk_id]),201


@app.route('/<int:pk>',methods = ['PUT','DELETE'])
def UpdateDelete_users(pk):
    detail = request.json
    if request.method == 'PUT':
        if pk not in users:
            return jsonify({"error": "User not found"}), 404
        users[pk] = {
            'name' : detail.get('name'),
            'age' : detail.get('age'),
            'designation' : detail.get('designation'),
            'skill' : detail.get('skill')
        }
        return jsonify(users[pk]),201
    elif request.method == 'DELETE':
        if pk not in users:
            return jsonify({"error": "User not found"}), 404
        users.pop(pk)
        return jsonify({"message": "User deleted"})


if __name__ == '__main__':
    app.run(debug=True)



