# Import statements
from flask import Flask, request, render_template
from flask.helpers import url_for
from flask_login import login_required, logout_user, login_user, current_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

# Sets up app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///music.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'keep it secret, keep it safe'
db = SQLAlchemy(app)

@login_manager.user_loader 
def load_user(user_id): 
    return Users.query.filter_by(id = user_id).first()

# User table
class Users(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

    def get_id(self):
        return self.id

# Songs table
class Songs(db.Model):
    __tablename__ = "Songs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    albumkey = db.Column(db.Integer)
    genrekey = db.Column(db.Integer, nullable = False)
    artistkey = db.Column(db.Integer, nullable = False)

# Playlists table
class Playlists(db.Model):
    __tablename__ = "Playlists"
    id = db.Column(db.Integer, primary_key = True)
    userkey = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String, nullable = False)
    public = db.Column(db.Integer, nullable = False)

# Login
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        user = Users.query.filter_by(username=data['username']).first() 
        if user is None or not user.check_password(data['password']): 
            return (url_for('login'))[1:]
        login_user(user)
        if user.username == "admin":
            return url_for("admin")[1:]
        else:
            return url_for("home")[1:]
    elif request.method == "GET":   
        return render_template('login.html')

# Admin
@app.route("/admin", methods = ["GET", "POST", "PUT", "DELETE"])
def admin():
    return "Admin"

# Home
@app.route("/home", methods = ["GET"])
def home():
    return "Home"

# Runs app
if __name__ == "__main__":
    #db.create_all() # Only need this line if db not created
    app.run(debug=True)