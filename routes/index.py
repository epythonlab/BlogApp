from app import app

from flask import render_template, flash, request, url_for, redirect
from datetime import date
from models.Post import *
@app.route('/')
def index():
    # get data from database
    post_data = db.session.query(Post).order_by(Post.id.desc()).all()


    return render_template('index.html', posts = post_data)

# create route to post.html
@app.route('/post/')
def post():

    return render_template('post.html')

# route to create post
@app.route('/create_post', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        # get form valuesPost successfuly created!
        title = request.form['title']
        desc = request.form['desc']
        p_date = date.today()

        # save to the database
        Post.create({
        'title': title,
        'desc' : desc,
        'p_date': p_date
        })

        # flash message
        flash("Post successfuly created!")
        return redirect(url_for('post'))
