#!/Users/ewilens/anaconda3/bin/python3

from flask import Flask, render_template
app = Flask(__name__) # __name__ is just the name of the current module, helps flask find libraries/static files

@app.route('/') # create home route. Browser will display whatever is returned from the following function
@app.route('/home') # make it so / and /home go to the same place
def home_page():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
