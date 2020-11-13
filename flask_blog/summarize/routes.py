from flask import render_template, flash, Blueprint
from flask_blog.summarize.forms import SummarizeForm

summarize = Blueprint('summarize', __name__)


@summarize.route('/summarize-text', methods=['GET', 'POST'])
def summarize_text():
    """ This route will hold the NLP Text Summarize module. """
    form = SummarizeForm()
    if form.validate_on_submit():
        full_text = form.full_text.data
        summarize_text =

    return render_template('summarize.html', form=form title='Summarize Text')
