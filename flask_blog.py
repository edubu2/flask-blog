from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # __name__ is just the name of the current module, helps flask find libraries/static files

# Use secret key (created by random in terminal w/ python secrets)
app.config['SECRET_KEY'] = '2c6f7da15b2e9db5e91dd289c8e75a9f'

# Database Config:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User({}, {}, {})".format(self.username, self.email, self.image_file)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr(self):
        return "{}, {}".format(self.title, self.date_posted)

# for now let's pretend we made a db call to retrieve this list of posts
posts = [
    {
        'author': 'Elliot Wilens',
        'title': 'Learning Flask part 1',
        'content': 'First post content',
        'date_posted': 'October 27, 2020'
    },
    {
        'author': 'Megan Harpell',
        'title': "I love Elliot's new site!",
        'content': "Elliot's site is dope. Super fly, even.",
        'date_posted': 'October 28, 2020'
    }
]

@app.route('/') # create home route. Browser will display whatever is returned from the following function
@app.route('/home') # make it so / and /home go to the same place
def home():
    return render_template('home.html', posts=posts) # we can now access this variable in the template using arg name 'posts'

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # if the form was valid when it was submitted:
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # fake data to simulate successful login
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You're logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please Check Username & Password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

print(type(render_template))
