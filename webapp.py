#adapted from https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example

from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
socketio = SocketIO(app, async_mode=None)

@app.route('/')
def index():
    return render_template('home.html', async_mode=socketio.async_mode)


@socketio.on('connect')
def test_connect():
    new_user = request.args['username']
    emit('start', 'You joined as ' + new_user) #send data to the client that just connected
    #to use emit: emit(event, data)
    socketio.emit('new_user_event', new_user) #send data to ALL clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
