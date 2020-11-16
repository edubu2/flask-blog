from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flask_blog import db
from flask_blog.models import Post
from flask_blog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    """This route is where users will add new posts to the blog."""
    form = PostForm()
    if form.validate_on_submit():
        # create instance of Post class w/ this post's content. I could have expressed the 'user_id=current_user' attribute as 'author=current_user' instead, since it's backref to class User.
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend_name='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    # grab the post from the db. If it doesn't exist, return 404 error ('page doesn't exist')
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """This route is where users can modify their existing posts """
    # grab the post from the db. If it doesn't exist, return 404 error ('page doesn't exist')
    post = Post.query.get_or_404(post_id)
    # Ensure the editor is actually the author of the post
    if post.author != current_user:
        abort(403)  # 403 is HTTP response for a forbidden route.
    form = PostForm()
    # If it's a POST request (meaning user submitted the form), update DB if the changes are valid.
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    # Otherwise (GET request), pre-populate form with existing post data
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend_name='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    """This route allows users to delete posts """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.home'))
