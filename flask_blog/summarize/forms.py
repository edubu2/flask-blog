from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError
from wtforms import SubmitField, TextAreaField


class SummarizeForm(FlaskForm):
    full_text = TextAreaField('Long text', validators=[DataRequired()])
    summary = TextAreaField('Summary', render_kw={"cols":35, "rows":12})
    submit = SubmitField('Summarize')

    def validate_text_length(self, full_text):
        """Ensures the user's text input is long enough to generate a strong summary. """

        if len(full_text) < 1000:
            raise ValidationError(
                "Text is not long enough to generate a summary.")
