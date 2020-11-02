from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
