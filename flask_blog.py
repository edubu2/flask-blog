from flask import Flask # import Flask class
app = Flask(__name__) # __name__ is just the name of the current module, helps flask find libraries/static files


@app.route('/') # create routes. These are what are used by our browser to go to different pages
def hello_world():
    return 'Hello, World!'
