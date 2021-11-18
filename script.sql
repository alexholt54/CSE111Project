-- Delete all tables
DROP TABLE IF EXISTS Genres;
DROP TABLE IF EXISTS Songs;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Playlists;
DROP TABLE IF EXISTS Followers;
DROP TABLE IF EXISTS FollowersArtists;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS PlaylistsSongs;

-- Create tables
CREATE TABLE Genres (
    g_key INTEGER PRIMARY KEY,
    g_name VARCHAR(50) NOT NULL
);

CREATE TABLE Songs (
    s_key INTEGER PRIMARY KEY,
    s_name VARCHAR(200) NOT NULL,
    s_albumkey INT,
    s_genrekey INT NOT NULL,
    s_artistkey INT NOT NULL
);

CREATE TABLE Albums (
    al_key INTEGER PRIMARY KEY,
    al_name VARCHAR(200) NOT NULL,
    al_year INT
);

CREATE TABLE Playlists (
    p_key INTEGER PRIMARY KEY,
    p_userkey INT NOT NULL,
    p_name VARCHAR(50) NOT NULL,
    p_public INT NOT NULL
);

CREATE TABLE PlaylistsSongs (
    ps_pkey INT,
    ps_skey INT,
    PRIMARY KEY (ps_pkey, ps_skey)
);

CREATE TABLE Followers (
    f_key INT,
    f_userkey INT,
    PRIMARY KEY (f_key, f_userkey)
);

CREATE TABLE FollowersArtists (
    fa_key INT,
    fa_artistkey INT,
    PRIMARY KEY (fa_key, fa_artistkey)
);

CREATE TABLE Users (
    u_key INTEGER PRIMARY KEY,
    u_username VARCHAR(30) NOT NULL UNIQUE,
    u_password VARCHAR(100) NOT NULL
);

CREATE TABLE Artists (
    ar_key INTEGER PRIMARY KEY,
    ar_name VARCHAR(100) NOT NULL
);

-- Populate tables
INSERT INTO Genres (g_name)
values('HipHop');

INSERT INTO Genres (g_name)
values('Pop');

INSERT INTO Genres (g_name)
values('R&B');

INSERT INTO Genres (g_name)
values('Electronic');

INSERT INTO Genres (g_name)
values('K-Pop');

INSERT INTO Genres (g_name)
values('Metal');

INSERT INTO Genres (g_name)
values('Rock');

INSERT INTO Genres (g_name)
values('Country');

INSERT INTO Genres (g_name)
values('Alternative');

INSERT INTO Genres (g_name)
values('Indie');



INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Lose Yourself', 1, 1, 1);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Like Toy Soliders', 1, 1, 1);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Sicko Mode', 2, 1, 2);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Back in Black', 3, 6, 3);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Pink + White', 4, 3, 4);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Call Out My Name', 5, 3, 5);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('StarBoy', 6, 3, 5);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Bad Blood', 7, 2, 6);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Bangarang', 8, 4, 7);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Telephones', 9, 10, 8);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Small Town Small', 10, 8, 9);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Boys With Luv', 1, 5, 10);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Livin on a Prayer', 12, 7, 11);

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Superstar', 13, 10, 12);



INSERT INTO Albums (al_name,al_year)
values('Curtain Call - Hits(Deluxe Version)', 2005);

INSERT INTO Albums (al_name,al_year)
values('AstroWorld', 2018);

INSERT INTO Albums (al_name,al_year)
values('Back In Black', 1980);

INSERT INTO Albums (al_name,al_year)
values('Blonde', 2016);

INSERT INTO Albums (al_name,al_year)
values('My Dear Melancholy', 2018);

INSERT INTO Albums (al_name,al_year)
values('Starboy', 2016);

INSERT INTO Albums (al_name,al_year)
values('1989', 2014);

INSERT INTO Albums (al_name,al_year)
values('Bangarang', 2011);

INSERT INTO Albums (al_name,al_year)
values('Changes', 2018);

INSERT INTO Albums (al_name,al_year)
values('MACON', 2021);

INSERT INTO Albums (al_name,al_year)
values('One Twice Melody', 2022);

INSERT INTO Albums (al_name,al_year)
values('Slippery When Wet', 1986);

INSERT INTO Albums (al_name,al_year)
values('MAP OF THE SOUL', 2019);



INSERT INTO Artists (ar_name)
values('Eminem');

INSERT INTO Artists (ar_name)
values('Travis Scott');

INSERT INTO Artists (ar_name)
values('AC/DC');

INSERT INTO Artists (ar_name)
values('Frank Ocean');

INSERT INTO Artists (ar_name)
values('The Weeknd');

INSERT INTO Artists (ar_name)
values('Taylor Swift');

INSERT INTO Artists (ar_name)
values('Skrillex');

INSERT INTO Artists (ar_name)
values('Vacations');

INSERT INTO Artists (ar_name)
values('Jason Aldean');

INSERT INTO Artists (ar_name)
values('BTS');

INSERT INTO Artists (ar_name)
values('Bon Jovi');

INSERT INTO Artists (ar_name)
values('Beach House');



INSERT INTO Users (u_username,u_password)
values('RyanS', 'ILML');

INSERT INTO Users (u_username,u_password)
values('AlexH', '#LoveWins');

INSERT INTO Users (u_username,u_password)
values('TheLad', 'Xbox1');

INSERT INTO Users (u_username,u_password)
values('Muska', 'Clash101');

INSERT INTO Users (u_username,u_password)
values('Immortal', 'CoffeeCup');

INSERT INTO Users (u_username,u_password)
values('MasterChief', 'Cortana');

INSERT INTO Users (u_username,u_password)
values('JackBoy', 'Cactus');

INSERT INTO Users (u_username,u_password)
values('Santosh', 'CSE20');

INSERT INTO Users (u_username,u_password)
values('ImLikeThat', 'JustDoIt');

INSERT INTO Users (u_username,u_password)
values('TimCook', 'Apple');



INSERT INTO Followers
values(1, 2);

INSERT INTO Followers
values(1, 10);

INSERT INTO Followers
values(1, 6);

INSERT INTO Followers
values(2, 1);

INSERT INTO Followers
values(2, 10);

INSERT INTO Followers
values(2, 8);

INSERT INTO Followers
values(2, 6);

INSERT INTO Followers
values(3, 4);

INSERT INTO Followers
values(3, 1);

INSERT INTO Followers
values(3, 6);

INSERT INTO Followers
values(4, 1);

INSERT INTO Followers
values(4, 3);

INSERT INTO Followers
values(4, 6);

INSERT INTO Followers
values(4, 8);

INSERT INTO Followers
values(5, 7);

INSERT INTO Followers
values(6, 1);

INSERT INTO Followers
values(6, 4);

INSERT INTO Followers
values(7, 2);

INSERT INTO Followers
values(7, 5);

INSERT INTO Followers
values(8, 2);

INSERT INTO Followers
values(8, 3);

INSERT INTO Followers
values(8, 4);

INSERT INTO Followers
values(9, 5);

INSERT INTO Followers
values(10, 1);



INSERT INTO FollowersArtists
VALUES (1, 1);

INSERT INTO FollowersArtists
VALUES (1, 2);

INSERT INTO FollowersArtists
VALUES (1, 3);

INSERT INTO FollowersArtists
VALUES (2, 1);

INSERT INTO FollowersArtists
VALUES (3, 11);

INSERT INTO FollowersArtists
VALUES (3, 4);

INSERT INTO FollowersArtists
VALUES (4, 1);

INSERT INTO FollowersArtists
VALUES (5, 6);

INSERT INTO FollowersArtists
VALUES (6, 10);

INSERT INTO FollowersArtists
VALUES (7, 9);



INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(1, 'Vibezz', 0);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(1, 'Music', 0);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(2, 'Heat', 1);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(3, 'Chillin', 1);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(4, 'Only Bangerz', 1);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(5, 'My Playlist', 1);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(6, 'Feelz', 0);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(7, 'Down Atrocious', 0);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(8, 'Top Hits', 1);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(9, 'Lofi', 0);

INSERT INTO Playlists (p_userkey, p_name, p_public)
VALUES(10, 'Slaps', 1);

INSERT INTO PlaylistsSongs
VALUES(1, 1);

INSERT INTO PlaylistsSongs
VALUES(2, 6);

INSERT INTO PlaylistsSongs
VALUES(3, 3);

INSERT INTO PlaylistsSongs
VALUES(4, 2);

INSERT INTO PlaylistsSongs
VALUES(6, 5);

INSERT INTO PlaylistsSongs
VALUES(7, 7);

INSERT INTO PlaylistsSongs
VALUES(8, 8);

INSERT INTO PlaylistsSongs
VALUES(9, 10);

INSERT INTO PlaylistsSongs
VALUES(10, 9);



-- Create user
INSERT INTO Users (u_username, u_password)
VALUES('test_name', 'test_password');



-- Delete user "RyanS"
DELETE FROM PlaylistsSongs
WHERE ps_pkey in (SELECT p_key FROM Users, Playlists WHERE u_key = p_userkey AND u_username = "RyanS");

DELETE FROM Playlists
WHERE p_userkey = (SELECT u_key FROM Users WHERE u_username = 'RyanS');

DELETE FROM Followers
WHERE f_key = (SELECT u_key FROM Users WHERE u_username = 'RyanS')
OR f_userkey = (SELECT u_key FROM Users WHERE u_ussername = 'RyanS');

DELETE FROM FollowersArtists
WHERE fa_key = (SELECT u_key FROM Users WHERE u_username = 'RyanS');

DELETE FROM Users
WHERE u_username = 'RyanS';



-- Logging in
SELECT *
FROM Users
WHERE u_username = 'RyanS'
    AND u_password = 'ILML';



-- User "Immortal" follows "TimCook"
insert into Followers
select user1.u_key, user2.u_key
from Users user1, Users user2
where user1.u_username = 'Immortal'
    and user2.u_username = 'TimCook';



-- User "AlexH" unfollows "TheLad"
delete from Followers
where f_key = (select u_key from Users where u_username = 'AlexH')
    and f_userkey = (select u_key from Users where u_username = 'TheLad');



-- User "Muska" follows "Bon Jovi"
insert into FollowersArtists
select u_key, ar_key
from users, Artists
where u_username = 'Muska'
    and ar_name = 'Bon Jovi';



-- User "Muska" unfollows "Travis Scott"
delete from FollowersArtists
where fa_key = (select u_key from Users where u_username = 'Muska')
    and fa_artistkey = (select ar_key from Artists where ar_name = 'Travis Scott');



-- User "MasterChief" creates public "Halo" playlist
insert into Playlists (p_userkey, p_name, p_public)
select u_key, 'Halo', 1
from Users
where u_username = 'MasterChief';



-- Adding "Lose Yourself" to "Halo" playlist
insert into PlaylistsSongs
select p_key, s_key
from Songs, Playlists
    where p_name = 'Halo'
    and s_name = 'Lose Yourself';



-- Removing "Bangarang" from "Lofi" playlist
delete from PlaylistsSongs
select p_key, s_key
from Songs, Playlists
    where s_name = 'Bangarang'
    and p_name = 'Lofi';



-- Deleting "Lofi" playlist
delete from PlaylistsSongs
where ps_pkey = (select p_key from Playlists where p_name = 'Lofi');
delete from Playlists
where p_name = 'Lofi';



-- Getting all of User "Santosh's" followers
select followers.u_username
from Users followers, Users account, Followers
where followers.u_key = Followers.f_key
    and account.u_key = Followers.f_userkey
    and account.u_username = 'Santosh';



-- Getting who User "Santosh" is following
select account.u_username
from Users followers, Users account, Followers
where followers.u_key = Followers.f_key
    and account.u_key = Followers.f_userkey
    and followers.u_username = 'Santosh';



-- Getting all of User "JackBoy's" followed artists
select ar_name
from Users, FollowersArtists, Artists
where u_key = fa_key
    and fa_artistkey = ar_key
    and u_username = 'JackBoy';



-- Adding all songs with "HipHop" genre to "Only Bangerz" playlist
insert into PlaylistsSongs
select p_key, s_key
from Playlists, Songs, Genres
where p_name = 'Only Bangerz'
    and s_genrekey = g_key
    and g_name = 'HipHop';



-- Removing all songs with "Country" genre from "Vibezz"
delete from PlaylistsSongs
where p_key = (select p_key from Playlists where p_name = "Vibezz")
    and s_key in (select s_key from Songs, Genres where s_genrekey = g_key and g_name = "Country")



-- Adding all songs by "The Weeknd" to "Feelz" playlist
insert into PlaylistsSongs
select p_key, s_key
from Playlists, Songs, Artists
where p_name = 'Feelz'
    and s_artistkey = ar_key
    and ar_name = 'The Weeknd';



-- Adding all songs from album "1989" into "Down Atrocious" playlist
insert into PlaylistsSongs
select p_key, s_key
from Playlists, Songs, Albums
where p_name = 'Down Atrocious'
    and s_albumkey = al_key
    and al_name = '1989';



-- Copy all songs from "Top Hits" playlist into "Slaps" playlist
insert into PlaylistsSongs
select new.p_key, ps_skey
from Playlists new, PlaylistsSongs, Playlists copying
where new.p_name = 'Slaps'
    and copying.p_key = ps_pkey
    and copying.p_name = "Top Hits"

