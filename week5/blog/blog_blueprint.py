from email.utils import format_datetime
from flask import Blueprint, flash, redirect, render_template as render, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from model.db import db


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return f"BlogPost('{self.title, self.author, self.date_posted}')"
    
    
    @classmethod
    def create_from_form(cls, form):
        return cls(title=form.title.data, content=form.content.data)

blog_blueprint = Blueprint('blog_blueprint', __name__, template_folder='templates')

blog_posts = [
    {'id': 1, 'title': 'First Post', 'content': 'Content Here' , 'date': str('2024-09-01')},
    {'id': 2, 'title': 'Second Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 3, 'title': 'Third Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 4, 'title': 'Fourth Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 5, 'title': 'Fifth Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 6, 'title': 'Sixth Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 7, 'title': 'Seventh Post', 'content': 'Content Here', 'date':'2024-09-01'},
]

_date = datetime.today().strftime('%Y-%m-%d')

class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit")




@blog_blueprint.route("/posts")
def post():
    posts = [
        {'id': 1, 'title':'First Post', 'content':'first post content'},
    ]
    return render('blog/post_details.html')



@blog_blueprint.route('/post/<int:post_id>')
def post_detail(post_id):
    post = {}
    return render('blog/post_detail.html', data={'post': post})



@blog_blueprint.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = BlogPostForm()
    db_session = db.session

    if form.validate_on_submit():
        post = BlogPost(**{field.name: field.data for field in form if field.name not in ['submit', 'csrf_token']}, date_posted=datetime.today())
        
        db_session.add(post)
        db_session.commit()

        flash("Post created successfully", "success")
        return redirect(url_for('blog_blueprint.create_post'))
    
    if form.errors:
        flash(f"Form Errors {form.errors}", "danger")

    return render('blog/create_post.html', form=form)