from flask import Blueprint, flash, redirect, render_template as render, url_for
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from wtforms import PasswordField, StringField, SubmitField
from flask_wtf import FlaskForm
import email_validator
from wtforms.validators import DataRequired, Email, Length, EqualTo
from model.db import db
from server_app import app

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates')

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


    def set_password(self, password):
        return password

login_manager = LoginManager(app)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


@auth_blueprint.route("/jklogin")
@login_manager.user_loader
def load_user(user_id):

    login = [
        
    ]
    
    return User.query.get(int(user_id))

# def set

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()
        flash("Account Created Successfully", "success")
        return redirect(url_for('login'))
    return render('users/register.html', form=form)

# return render("users/login.html", data={"login":login})

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        if user.set_password(form.password.data):
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('invalid details', 'error')
    return render('users/login.html', form=form)


@auth_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render('users/profile.html')

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))