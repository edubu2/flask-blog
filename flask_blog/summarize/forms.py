from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, TextAreaField


class SummarizeForm(FlaskForm):
    full_text = TextAreaField('Long text', validators=[DataRequired])
    summary = TextAreaField('Summary')
    submit = SubmitField('Summarize')
