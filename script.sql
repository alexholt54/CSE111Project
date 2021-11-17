-- Delete all tables
DROP TABLE IF EXISTS Genres;
DROP TABLE IF EXISTS Songs;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Playlists;
DROP TABLE IF EXISTS Followers;
DROP TABLE IF EXISTS FollowersArtists;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Artists;

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
    p_key INT,
    p_userkey INT,
    p_songkey INT,
    p_public INT NOT NULL,
    PRIMARY KEY (p_key, p_userkey, p_songkey)
);

CREATE TABLE Followers (
    f_key INT,
    f_userkey INT,
    PRIMARY KEY (f_key, f_userkey)
);

CREATE TABLE FollowersArtists (
    f_key INT,
    f_artistkey INT,
    PRIMARY KEY (f_key, f_artistkey)
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
values('Lose Yourself', '1', '1', '1');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Like Toy Soliders', '1', '1', '1');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Sicko Mode', '2', '1', '2');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Back in Black', '3', '6', '3');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Pink + White', '4', '3', '4');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Call Out My Name', '5', '3', '5');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('StarBoy', '6', '3', '5');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Bad Blood', '7', '2', '6');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Bangarang', '8', '4', '7');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Telephones', '9', '10', '8');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Small Town Small', '10', '8', '9');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Boys With Luv', '11', '5', '10');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Livin on a Prayer', '12', '7', '11');

INSERT INTO Songs (s_name,s_albumkey,s_genrekey,s_artistkey)
values('Superstar', '13', '10', '12');



INSERT INTO Albums (al_name,al_year)
values('Curtain Call - Hits(Deluxe Version)', '2005');

INSERT INTO Albums (al_name,al_year)
values('AstroWorld', '2018');

INSERT INTO Albums (al_name,al_year)
values('Back In Black', '1980');

INSERT INTO Albums (al_name,al_year)
values('Blonde', '2016');

INSERT INTO Albums (al_name,al_year)
values('My Dear Melancholy', '2018');

INSERT INTO Albums (al_name,al_year)
values('Starboy', '2016');

INSERT INTO Albums (al_name,al_year)
values('1989', '2014');

INSERT INTO Albums (al_name,al_year)
values('Bangarang', '2011');

INSERT INTO Albums (al_name,al_year)
values('Changes', '2018');

INSERT INTO Albums (al_name,al_year)
values('MACON', '2021');

INSERT INTO Albums (al_name,al_year)
values('One Twice Melody', '2022');

INSERT INTO Albums (al_name,al_year)
values('Slippery When Wet', '1986');

INSERT INTO Albums (al_name,al_year)
values('MAP OF THE SOUL', '2019');



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
values('1', '2');

INSERT INTO Followers
values('1', '10');

INSERT INTO Followers
values('1', '6');

INSERT INTO Followers
values('2', '1');

INSERT INTO Followers
values('2', '10');

INSERT INTO Followers
values('2', '8');

INSERT INTO Followers
values('2', '6');

INSERT INTO Followers
values('3', '4');

INSERT INTO Followers
values('3', '1');

INSERT INTO Followers
values('3', '6');

INSERT INTO Followers
values('4', '1');

INSERT INTO Followers
values('4', '3');

INSERT INTO Followers
values('4', '6');

INSERT INTO Followers
values('4', '8');

INSERT INTO Followers
values('5', '7');

INSERT INTO Followers
values('6', '1');

INSERT INTO Followers
values('6', '4');

INSERT INTO Followers
values('7', '2');

INSERT INTO Followers
values('7', '5');

INSERT INTO Followers
values('8', '2');

INSERT INTO Followers
values('8', '3');

INSERT INTO Followers
values('8', '4');

INSERT INTO Followers
values('9', '5');

INSERT INTO Followers
values('10', '1');



INSERT INTO Playlists
values('1', '1', '1', '0');

INSERT INTO Playlists
values('2', '2', '6', '1');

INSERT INTO Playlists
values('3', '3', '3', '1');

INSERT INTO Playlists
values('4', '4', '2', '1');

INSERT INTO Playlists
values('5', '5', '4', '1');

INSERT INTO Playlists
values('6', '6', '5', '0');

INSERT INTO Playlists
values('7', '7', '7', '0');

INSERT INTO Playlists
values('8', '8', '8', '1');

INSERT INTO Playlists
values('9', '9', '10', '0');

INSERT INTO Playlists
values('10', '10', '9', '1');

-- Create user
INSERT INTO Users (u_username, u_password)
VALUES('test_name', 'test_password');

-- Logging in
SELECT *
FROM Users
WHERE u_username = 'RyanS'
    AND u_password = 'ILML';

-- 