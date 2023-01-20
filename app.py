# http://127.0.0.1:5000
# This is a minimal example of server-side updates using socketio and flask,

# there are just two files! You run the flask app and then can see the pushes in your browser.

# Where this will be useful is if you don't want the clients polling,
# e.g. you don't want to use setInterval on javascript, you want the backend
# in charge of when new events are emited.

# On the backend (in flask) it chooses a random number once per second (this function is meant to stand
# in for any other event you might have).

# If the random number 1-100 is less than 90 (you can reduce this to reduce chances
# of a broadcast) the server pushes the mssage and the front end receives it.

from flask import Flask, render_template, jsonify
import random
import time
from flask_socketio import SocketIO

print("Application started. Just navigate to http://127.0.0.1:5000 to use.")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gj73sdf4hdffvg2w6rubnws3cs24fsd63fveoiuc2dfhg6bhad'
socketio = SocketIO(app)

# The next function is the one that sends the notification. 
# For our purposes we call it again after a second but in your app you could have a different way in
# which it is called.

def server_side_send(interval):
    number = random.randint(1, 100)
    socketio.emit('my_event', number)
    time.sleep(interval)
        
    
    t = time.localtime()
    print("Emitting event from server side! Random number is ", number , "emitted at ",  time.strftime("%H:%M:%S", t))
    socketio.start_background_task(target=server_side_send, interval=1) # call same function a second later
    return


@socketio.on('connect')
def handle_connect():
    print ("TOTALLY GOT A NEW CONNECTION!!!!")
    server_side_send(interval=1)

@socketio.on('my_event')
def handle_my_event(json):
    print('---my_event event')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def random_number():
    number = random.randint(1, 100)
    if number < 90: # lower 90 to send less frequently, e.g. 2 would only send 2% of the time.
        return jsonify(number=number)
    else:
        return jsonify(number=None)

if __name__ == '__main__':
    socketio.run(app)