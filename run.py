from app import app, views
port = 5000
app.run("localhost", debug = True, port = port, threaded = True)
