from flask import Flask, flash, redirect, render_template as render, url_for
# from jinja2 import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"


def format_date(date):
    return datetime(date).strftime('%B %d, %Y')

app.jinja_env.globals.update(format_date=format_date)


blog_posts = [
    {'id': 1, 'title': 'First Post', 'content': 'Content Here' , 'date': format_date('2024-09-01')},
    {'id': 2, 'title': 'Second Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 3, 'title': 'Third Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 4, 'title': 'Fourth Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 5, 'title': 'Fifth Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 6, 'title': 'Sixth Post', 'content': 'Content Here', 'date':'2024-09-01'},
    {'id': 7, 'title': 'Seventh Post', 'content': 'Content Here', 'date':'2024-09-01'}
]



class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Create Post")



@app.route("/")
def home():
    return render("home.html")

@app.route("/blog")
def blog():
    return render('blog.html', posts=blog_posts)

@app.route("/create_post", methods=['GET', 'POST'])
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        return redirect(url_for('home'))

    return render('create_post.html', form  = form)

    

@app.route("/about")
def about():
    return render("home.html")

@app.route('/login', methods=["POST"])
def login():
    authentication_successful = True

    if authentication_successful:
        flash("Login Successful", "success")
    else:
        flash("Invalid Credentials", "error")


if __name__ == "__main__":
    app.run()