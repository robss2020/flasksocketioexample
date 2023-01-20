![ Banner for this app, a visualization of receiving notifications](https://raw.githubusercontent.com/robss2020/flasksocketioexample/main/banner.png "Receiving notifications")

# Flask app that sends pushes server-side messages using SocketIO

## Motivation

One way to get server updates is to poll for them, e.g. using setInterval in JavaScript.

This can get out of hand though - do you really want all your clients polling your server
every time they have the website open, even if there is no message for them?

Do you want them to poll infrequently and thereby miss an instant update?

For some cases it is better for the server to decide when it wants to broadcast a message.

There are many solutions for this.  Some of them include:

- WebSockets
- Server-Sent Events (SSE)
- WebRTC

For this app we will use SocketIO, a great small library for Flask.
That means including a small javascript file.

## Files - front end and back-end

There are just two files, app.py and templates/index.html

- The back-end runs flask Flask and SocketIO (flask_socketio).
- The front-end also includes the socketio javascript library.

## Usage

Pull the repo.


Install required dependencies flask and flask_socketio
I like using pip install from within the Anaconda prompt:

   `pip install Flask flask_socketio`

Then start the app with 

`python app.py`

In any browser, navigate to http://127.0.0.1:5000 and you will see the console events there.

Hopefully this is enough for you to get this working in your app.

![ Screenshot of the app](https://raw.githubusercontent.com/robss2020/flasksocketioexample/main/screenshot.PNG "Screenshot of the app")


## Resources

- https://flask-socketio.readthedocs.io/en/latest/


## License
CC0 no rights reserved - this one is public domain, feel free to use this one in any
any way including commercial project without attribution.

https://creativecommons.org/share-your-work/public-domain/cc0/

If you're looking for a full-stack developer job inquiries appreciated: rviragh+tao@gmail.com

