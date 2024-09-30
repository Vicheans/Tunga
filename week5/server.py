from flask_migrate import Migrate
from blog.blog_blueprint import blog_blueprint
from auth.auth_blueprint import auth_blueprint
# from blog.views import posts
from model.db import db 
from server_app import app


app.config['SECRET_KEY'] = 'supersecretkey' #secures session cookie
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# db.drop_all() 
with app.app_context():
    # db.drop_all()
    db.create_all()

app.register_blueprint(blog_blueprint, url_prefix='/blog')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)

