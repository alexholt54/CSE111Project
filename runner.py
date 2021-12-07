# Import statements
from flask import Flask, request, render_template, templating
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
@app.route("/home", methods = ["GET", "POST"])
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
    elif request.method == "POST":
        return "success"

@app.route("/album/<album_name>")
@login_required
def album(album_name):
    album_name = album_name.replace("%20", " ")
    album = Albums.query.filter_by(name = album_name).first()
    if album is not None:
        if request.method == "GET":
            song = Songs.query.filter_by(albumkey = album.id).first()
            if song is not None:
                artist = Artists.query.filter_by(id = song.artistkey).first()
                artist = artist.name
                songs = Songs.query.filter_by(albumkey = album.id)
                return render_template("album.html", albumName = album_name, artist = artist, songs = songs)

@app.route("/user/<username>")
@login_required
def userpage(username):
    username = username.replace("%20", " ")
    user = Users.query.filter_by(username = username).first()
    isUser = False
    if user is not None:
        if user.id == current_user.id:
            isUser = True
        if request.method == "GET":
            listFollowers = []
            listFollowing = []
            listPlaylists = []
            listArtists = []
            followers = Followers.query.filter_by(followed = user.id)
            following = Followers.query.filter_by(user = user.id)
            for follower in followers:
                temp = Users.query.filter_by(id = follower.user).first()
                listFollowers.append(temp.username)
            for follower in following:
                temp = Users.query.filter_by(id = follower.followed).first()
                listFollowing.append(temp.username)

            if (current_user.id == user.id):
                playlists = Playlists.query.filter_by(userkey = user.id)
                for playlist in playlists:
                    listPlaylists.append(playlist.name)
            else:
                playlists = Playlists.query.filter_by(userkey = user.id, public = 1)
                for playlist in playlists:
                    listPlaylists.append(playlist.name)

            followedArtists = FollowersArtists.query.filter_by(userkey = user.id)
            for artist in followedArtists:
                temp = Artists.query.filter_by(id = artist.artistkey).first()
                listArtists.append(temp.name)

            return render_template("users.html", username = username, isUser = isUser, followers = listFollowers,
                                    following = listFollowing, playlists = listPlaylists, artists = listArtists)

@app.route("/artist/<artistname>", methods = ["GET", "POST", "DELETE"])
@login_required
def artistpage(artistname):
    artist = artistname.replace("%20", " ")
    artist = Artists.query.filter_by(name = artist).first()
    if request.method == "GET":
        if artist is not None:
            numFollowers = 0
            res = FollowersArtists.query.filter_by(artistkey = artist.id)
            for row in res:
                numFollowers = numFollowers + 1
            songs = Songs.query.filter_by(artistkey = artist.id)
            albums = []
            for song in songs:
                album = Albums.query.filter_by(id = song.albumkey).first()
                if album is not None:
                    if album.name not in albums:
                        albums.append(album.name)
            following = False
            follow = FollowersArtists.query.filter_by(userkey = current_user.id, artistkey = artist.id).first()
            if follow is not None:
                following = True
            return render_template("artist.html", artist = artist.name, numFollowers = numFollowers,
                                songs = songs, albums = albums, following = following)
    elif request.method == "POST":
        follow = FollowersArtists.query.filter_by(userkey = current_user.id, artistkey = artist.id).first()
        if follow is None:
            newFollow = FollowersArtists(current_user.id, artist.id)
            db.session.add(newFollow)
            db.session.commit()
            return "success"
    elif request.method == "DELETE":
        follow = FollowersArtists.query.filter_by(userkey = current_user.id, artistkey = artist.id).first()
        if follow is not None:
            db.session.delete(follow)
            db.session.commit()
            return "success"

@app.route("/playlist/<playlistname>", methods = ["GET", "POST", "DELETE"])
@login_required
def playlist(playlistname):
    playlistname = playlistname.replace("%20", " ")
    playlist = Playlists.query.filter_by(name = playlistname).first()
    if playlist is not None:
        if request.method == "GET":
            ownsPlaylist = False
            if playlist.userkey == current_user.id:
                ownsPlaylist = True
            if playlist.public == 1 or playlist.userkey == current_user.id:
                songs = PlaylistsSongs.query.filter_by(playlistkey = playlist.id)
                listSongs = []
                listArtists = []
                for song in songs:
                    song = Songs.query.filter_by(id = song.songkey).first()
                    if song is not None:
                        artist = Artists.query.filter_by(id = song.artistkey).first()
                        if artist is not None:
                            listSongs.append(song.name)
                            listArtists.append(artist.name)
                return render_template("playlist.html", playlist = playlist, songs = listSongs, artists = listArtists, length = len(listSongs), 
                                    ownsPlaylist = ownsPlaylist)
        elif request.method == "POST":
            data = request.get_json()
            song = Songs.query.filter_by(name = data["song"]).first()
            if song is not None:
                newSong = PlaylistsSongs(playlist.id, song.id)
                db.session.add(newSong)
                db.session.commit()
                return "success"
        elif request.method == "DELETE":
            data = request.get_json()
            if data["type"] == "playlist":
                songs = PlaylistsSongs.query.filter_by(playlistkey = playlist.id)
                for song in songs:
                    db.session.delete(song)
                db.session.delete(playlist)
                db.session.commit()
                return "success"
            elif data["type"] == "song":
                data = request.get_json()
                song = Songs.query.filter_by(name = data["song"]).first()
                deleteSong = PlaylistsSongs.query.filter_by(playlistkey = playlist.id, songkey = song.id).first()
                db.session.delete(deleteSong)
                db.session.commit()
                return "success"

# Runs app
if __name__ == "__main__":
    #db.create_all() # Only need this line if db not created
    app.run(debug=True)