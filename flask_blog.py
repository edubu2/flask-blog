#!/Users/ewilens/anaconda3/bin/python3

from flask import Flask # import Flask class
app = Flask(__name__) # __name__ is just the name of the current module, helps flask find libraries/static files

@app.route('/') # create home route. Browser will display whatever is returned from the following function
def hello_world():
    return '<h1>Home Page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
