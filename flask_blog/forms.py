from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User

class RegistrationForm(FlaskForm):
    # username field (requires wtforms StringField, and length validator imports)
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    # email field (requires wtforms StringField, and email validator imports)
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # password field & confirm password fields (requires PasswordField, EqualTo validator imports to confirm passwords match)
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validations:
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:        # True if user is NOT empty, False otherwise
            raise ValidationError('Username is already taken. Please choose a different one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:        # True if user is NOT empty, False otherwise
            raise ValidationError('Email address is already taken. Please choose a different email address.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
