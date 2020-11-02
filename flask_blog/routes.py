from flask import render_template, url_for, flash, redirect
from flask_blog import app, db, bcrypt # these come from __init__.py
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post
from flask_login import login_user, current_user, logout_user

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # Check if user exists & the password is valid. If so, login. Otherwise, flash error.
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email & password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
