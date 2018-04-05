#adapted from https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example

from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
socketio = SocketIO(app, async_mode=None)
thread = None
thread_lock = Lock()


def background_thread():
    count = 0
    while True:
        socketio.sleep(5) #wait 5 seconds
        count += 1 #add 1 to count
        socketio.emit('count_event', count) #send count to ALL clients (see Broadcasting section of https://flask-socketio.readthedocs.io/en/latest/)

@app.route('/')
def index():
    return render_template('home.html', async_mode=socketio.async_mode)


@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock: #lock thread in case multiple clients are connecting at the same time
        #create one thread for all clients
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)
    emit('start', 'Connected') #send data to the client that just connected
    #to use emit: emit(event, data)

if __name__ == '__main__':
    socketio.run(app, debug=True)