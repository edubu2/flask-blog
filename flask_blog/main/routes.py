from flask import render_template, request, Blueprint
from flask_blog.models import Post

main = Blueprint('main', __name__)

@main.route('/') # create home route. Browser will display whatever is returned from the following function
@main.route('/home') # make it so / and /home go to the same place
def home():
    """This route is the home/default landing page for website and can be accessed with '/' or '/home' """
    page = request.args.get('page', 1, type=int)
    # Show 5 posts per page, ordered by date posted
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts) # we can now access this variable in the template using arg name 'posts'

@main.route('/about')
def about():
    return render_template('about.html', title='About')