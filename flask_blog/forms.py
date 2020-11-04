from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Ensures username doesn't already exist in DB"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')
    def validate_email(self, email):
        """Ensures email address doesn't already exist in DB"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address is already taken. Please choose a different email address.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'jpeg' 'png'])])
    submit = SubmitField('Update')

    # Custom validations:
    def validate_username(self, username):
        """First checks that the user changed their username. If so, make sure the new username isn't already taken."""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:        # True if user is NOT empty, False otherwise
                raise ValidationError('Username is already taken. Please choose a different one.')
    def validate_email(self, email):
        """First checks that the user changed their email address. If so, make sure the new email address isn't already taken."""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:        # True if user is NOT empty, False otherwise
                raise ValidationError('Email address is already taken. Please choose a different email address.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
