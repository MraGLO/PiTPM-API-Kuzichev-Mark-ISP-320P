from flask import Flask, request, jsonify
app = Flask(__name__)

user = []
music = []

@app.route('/')
def URLS():
    return "http://127.0.0.1:3005/user\n" + "   " + "http://127.0.0.1:3005/user/id\n" + "   " "http://127.0.0.1:3005/music\n" + "   " + "http://127.0.0.1:3005/music/id\n"
@app.route('/user', methods =['POST', 'GET'])
def Users():
    if request.method=='POST':

        data = request.get_json()

        name = data['name']
        surname = data['surname']
        email = data['email']
        address = data['address']
        telephone = data['telephone']
        user.append(name+" "+surname+" "+email+" "+address+" "+telephone)
        return "OK, 200"
    if request.method == 'GET':
        return user



@app.route('/user/<id>', methods =['PUT', 'DELETE'])
def UsersChange(id):
    if request.method=='DELETE':
        try:
            user.pop(int(id))
            return "OK, 200"
        except:
            return "Error, 500"
    if request.method == 'PUT':
        try:

            data = request.get_json()
            name = data['name']
            surname = data['surname']
            email = data['email']
            address = data['address']
            telephone = data['telephone']
            ch = name+" "+surname+" "+email+" "+address+" "+telephone
        
            user[int(id)]=ch   
            return "OK, 200"
        except:
            return "Error, 500"


@app.route('/music', methods =['POST', 'GET'])
def Musics():
    if request.method=='POST':

        data = request.get_json()

        name = data['name']
        author = data['author']
        date = data['date']
        genre = data['genre']
        music.append(name+" "+author+" "+date+" "+genre)
        return "OK, 200"
    if request.method == 'GET':
            return music

@app.route('/music/<id>', methods =['PUT', 'DELETE'])
def MusicsChange(id):
    if request.method=='DELETE':
        try:
            music.pop(int(id))
            return "OK, 200"
        except:
            return "Error, 500"
    if request.method == 'PUT':
        try:

            data = request.get_json()

            name = data['name']
            author = data['author']
            date = data['date']
            genre = data['genre']
            ch = name+" "+author+" "+date+" "+genre

            music[int(id)]=ch
            return "OK, 200"
        except:
            return "Error, 500"
                


if __name__ == '__main__':
    app.run(port=3005)
