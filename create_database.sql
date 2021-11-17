DROP TABLE IF EXISTS Genres;
DROP TABLE IF EXISTS Songs;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Playlists;
DROP TABLE IF EXISTS Followers;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Artists;

CREATE TABLE Genres (
    g_key INT PRIMARY KEY,
    g_name VARCHAR(50) NOT NULL
);

CREATE TABLE Songs (
    s_key INT PRIMARY KEY,
    s_name VARCHAR(200) NOT NULL,
    s_albumkey INT,
    s_genrekey INT NOT NULL,
    s_artistkey INT NOT NULL
);

CREATE TABLE Albums (
    al_key INT PRIMARY KEY,
    al_name VARCHAR(200) NOT NULL,
    al_year INT
);

CREATE TABLE Playlists (
    p_key INT PRIMARY KEY,
    p_userkey INT NOT NULL,
    p_songkey INT NOT NULL,
    p_public INT NOT NULL
);

CREATE TABLE Followers (
    f_key INT,
    f_userkey INT NOT NULL,
    PRIMARY KEY (f_key, f_userkey)
);

CREATE TABLE Users (
    u_key INT PRIMARY KEY,
    u_username VARCHAR(30) NOT NULL,
    u_password VARCHAR(100) NOT NULL
);

CREATE TABLE Artists (
    ar_key INT NOT NULL,
    ar_name VARCHAR(100) NOT NULL
);