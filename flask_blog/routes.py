from flask import render_template, url_for, flash, redirect
from flask_blog import app, db, bcrypt # these come from __init__.py
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
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
