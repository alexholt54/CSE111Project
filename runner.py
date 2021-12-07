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

    def __init__(self, name, albumkey, genrekey, artistkey):
        self.name = name
        self.albumkey = albumkey
        self.genrekey = genrekey
        self.artistkey = artistkey

# Playlists table
class Playlists(db.Model):
    __tablename__ = "Playlists"
    id = db.Column(db.Integer, primary_key = True)
    userkey = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String, nullable = False)
    public = db.Column(db.Integer, nullable = False)

    def __init__(self, userkey, name, public):
        self.userkey = userkey
        self.name = name
        self.public = public

# Genres table
class Genres(db.Model):
    __tablename__ = "Genres"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __init__(self, name):
        self.name = name

# Albums table
class Albums(db.Model):
    __tablename__ = "Albums"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    
    def __init__(self, name, year):
        self.name = name
        self.year = year

# Artists table
class Artists(db.Model):
    __tablename__ = "Artists"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __init__(self, name):
        self.name = name

# Followers table
class Followers(db.Model):
    __tablename__ = "Followers"
    user = db.Column(db.Integer, primary_key = True)
    followed = db.Column(db.Integer, primary_key = True)

    def __init__(self, user, followed):
        self.user = user
        self.followed = followed

# FollowersArtists table
class FollowersArtists(db.Model):
    __tablename__ = "FollowersArtists"
    userkey = db.Column(db.Integer, primary_key = True)
    artistkey = db.Column(db.Integer, primary_key = True)

    def __init__(self, userkey, artistkey):
        self.userkey = userkey
        self.artistkey = artistkey

class PlaylistsSongs(db.Model):
    __tablename__ = "PlaylistsSongs"
    playlistkey = db.Column(db.Integer, primary_key = True)
    songkey = db.Column(db.Integer, primary_key = True)

    def __init__(self, playlistkey, songkey):
        self.playlistkey = playlistkey
        self.songkey = songkey

# Log In
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
        return render_template("login.html")

# Log Out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return url_for('login')[1:]

# Create new user
@app.route("/newUser", methods = ["GET", "POST"])
def createUser():
    if request.method == "GET":
        return render_template("createUser.html")
    elif request.method == "POST":
        data = request.get_json()
        user = Users.query.filter_by(username=data["username"]).first()
        if user is None:
            user = Users(data["username"], data["password"])
            db.session.add(user)
            db.session.commit()
            return "success"

# Admin
@app.route("/admin", methods = ["GET", "POST", "PUT", "DELETE"])
@login_required
def admin():
    if request.method == "GET":
        users = Users.query.all()
        albums = Albums.query.all()
        artists = Artists.query.all()
        genres = Genres.query.all()
        playlists = Playlists.query.all()
        usernames_playlists = []
        for row in playlists:
            user = Users.query.filter_by(id = row.userkey).first()
            usernames_playlists.append(user.username)
        songs = Songs.query.all()

        song_albums = []
        song_genres = []
        song_artists = []
        for row in songs:
            album = Albums.query.filter_by(id = row.albumkey).first()
            genre = Genres.query.filter_by(id = row.genrekey).first()
            artist = Artists.query.filter_by(id = row.artistkey).first()
            song_albums.append(album.name)
            song_genres.append(genre.name)
            song_artists.append(artist.name)

        return render_template("admin.html", users = users, artists = artists, 
        genres = genres, playlists = playlists, usernames_playlists = usernames_playlists, 
        songs = songs, song_albums = song_albums, song_genres = song_genres, song_artists = song_artists)
    elif request.method == "POST":
        data = request.get_json()
        if data["type"] == "data":
            artist = Artists.query.filter_by(name = data["artist"]).first()
            song = Songs.query.filter_by(name = data["song"]).first()
            album = Albums.query.filter_by(name = data["album"]).first()
            genre = Genres.query.filter_by(name = data["genre"]).first()

            if artist is None:
                if data["artist"] != "":
                    newArtist = Artists(data["artist"])
                    db.session.add(newArtist)
                    db.session.commit()
                    artist = Artists.query.filter_by(name = data["artist"]).first()

            if album is None:
                if data["album"] != "" and data["year"] is not None:
                    newAlbum = Albums(data["album"], data["year"])
                    db.session.add(newAlbum)
                    db.session.commit()
                    album = Albums.query.filter_by(name = data["album"]).first()

            if genre is None:
                if data["genre"] != "":
                    newGenre = Genres(data["genre"])
                    db.session.add(newGenre)
                    db.session.commit()
                    genre = Genres.query.filter_by(name = data["genre"]).first()
                    
            if song is None:
                if data["song"] != "":
                    newSong = Songs(data["song"], album.id, genre.id, artist.id)
                    db.session.add(newSong)
                    db.session.commit()
            return "success"
    elif request.method == "DELETE":
        data = request.get_json()
        if data["type"] == "user":
            user = Users.query.filter_by(username = data["username"]).first()

            if user is not None:
                # Get id of user to be deleted
                deleteKey = user.id

                # Delete all user's followers and who they're following
                followers = Followers.query.filter((Followers.user == deleteKey) | (Followers.followed == deleteKey))
                if followers is not None:
                    for follower in followers:
                        db.session.delete(follower)

                # Delete the user's followed artists
                artists = FollowersArtists.query.filter_by(userkey = deleteKey)
                if artists is not None:
                    for artist in artists:
                        db.session.delete(artist)

                # Delete the user's playlists
                playlists = Playlists.query.filter_by(userkey = deleteKey)
                if playlists is not None:
                    for playlist in playlists:
                        # Delete songs from playlist being deleted
                        playlistSongs = PlaylistsSongs.query.filter_by(playlistkey = playlist.id)
                        for song in playlistSongs:
                            db.session.delete(song)
                        db.session.delete(playlist)

                # Now delete the user
                db.session.delete(user)
                db.session.commit()

                return "success"
        elif data["type"] == "data":

            return "success"

# Home
@app.route("/home")
@login_required
def home():
    if request.method == "GET":
        # Suggested followers

        res = db.session.execute("""
        select username
        from Users, Followers
        where id = followed
            and id != :key
            and user in (
                select followed
                from Followers
                where user = :key
            )
            and followed not in (
                select followed
                from Followers
                where user = :key
            )
        group by id
        order by count(*) desc
        limit 5;""", {"key" : current_user.id})

        accounts = []
        for row in res:
            accounts.append(row[0])


        res = db.session.execute("""
        select Artists.name
        from Artists, Songs, Genres
        where Artists.id = Songs.artistkey
            and Songs.genrekey = Genres.id
            and Genres.id in (
                select Genres.id
                from PlaylistsSongs, Songs, Genres, Playlists, Users
                where Users.id = :key
                    and songkey = Songs.id
                    and Songs.genrekey = Genres.id
                    and playlistkey = Playlists.id
                    and Playlists.userkey = Users.id
            )
            and Artists.id not in (
                select artistkey
                from FollowersArtists
                where userkey = :key
            )
        group by Artists.name, Genres.name
        order by count(*) desc
        limit 5;""",{"key" : current_user.id} )
        artists = []
        for row in res:
            artists.append(row[0])

        res = db.session.execute("""
        select Songs.name
        from Songs, PlaylistsSongs, Playlists
        where Playlists.public = 1
            and Playlists.userkey != :key
            and Playlists.id = playlistkey
            and Songs.id = songkey
            and Playlists.userkey in (
                select followed
                from Followers
                where user = :key
                )
            group by Songs.name
            order by count(*) desc
            limit 5;""", {"key" : current_user.id})
        followerRecs = []
        for row in res:
            followerRecs.append(row[0])

        return render_template("home.html", user = current_user, followers = accounts, artists = artists, followerRecs = followerRecs)

@app.route("/album/<album_name>")
@login_required
def album(album_name):
    if request.method == "GET":
        return render_template("album.html", albumName = album_name)

@app.route("/user/<username>")
@login_required
def userpage(username):
    if request.method == "GET":
        return render_template("users.html", username = username)

# Runs app
if __name__ == "__main__":
    #db.create_all() # Only need this line if db not created
    app.run(debug=True)