from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('home.html')

@socketio.on('connect')
def test_connect():
    print('a client connected')

@socketio.on('setUsername')
def set_username(new_user):
    print("here")
    print(new_user)
    emit('userJoined', new_user) #send the username back to the client as confirmation that they have joined
    #to use emit: emit(event, data)
    socketio.emit('newUserEvent', new_user) #send the new user's name to ALL clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
