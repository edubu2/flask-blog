from flask import render_template, flash, Blueprint
from flask_blog.summarize.forms import SummarizeForm
from flask_blog.summarize.utils import summarize_text

summarize = Blueprint('summarize', __name__)


@summarize.route('/summarize-text', methods=['GET', 'POST'])
def magic_summarize():
    """ This route allows users to get a summarized version of any long text (such as an article or email). """

    form = SummarizeForm()
    if form.validate_on_submit():
        full_text = form.full_text.data
        summary = summarize_text(full_text)
        form.summary.data = summary

    return render_template('summarize.html', form=form, title='Summarize Text', summary=summary)
