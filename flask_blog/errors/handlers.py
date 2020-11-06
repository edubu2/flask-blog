from flask import Blueprint, render_template

# Create errors blueprint instance. Don't forget to register these at the app's __init__.py file!
errors = Blueprint('errors', __name__)

# Create error handler decorators for 404, 403, and 500 errors.
@errors.app_errorhandler(404)
def error_404(error):
    # Note: Second value of returned statement = response_code (default=200)
    return render_template('errors/404.html'), 404 

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403 

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500 