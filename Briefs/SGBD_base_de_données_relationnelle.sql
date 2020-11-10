# 3 - Créer une base de données "netflix"
create database netflix;
use netflix;
# avant de creer les tables il faut ecrire sur le terminal mysql --local-infile=1 -u root -p/mysql --local-infile=1 -u ines -p
mysql --local-infile=1;

# 4 - Créer une table appelée ‘netflix_title’, importer les données provenant du fichier csv;


create table netflix_title (
	show_id int,
	type varchar(7),
	title varchar(104),
	director varchar(208),
	cast varchar(771),
	country varchar(123),
	date_added varchar(19),
	release_year int,
	rating varchar(8),
	duration varchar(10),
	listed_in varchar(79),
	description varchar(248));
    
#charger la table netflix_title;
load DATA LOCAL INFILE '/home/ines/Documents/CoursAnneLaure/1-SGBD/netflix_titles.csv'
INTO TABLE netflix_title
CHARACTER SET latin1
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
    
# Créer une table appelée ‘netflix_shows’ provenant du fichier Netflix Shows.csv 

CREATE TABLE netflix_shows (
    title VARCHAR (64),
    rating VARCHAR (9),
    ratingLevel VARCHAR (126),
    ratingDescription INT NOT NULL,
    release_year INT NOT NULL,
    user_rating_score VARCHAR (4),
    user_rating_size INT NOT NULL
);
    
# charger la table netflix_shows 
LOAD DATA LOCAL INFILE '/home/ines/Documents/CoursAnneLaure/1-SGBD/Netflix_Shows.csv'
INTO TABLE netflix_shows
CHARACTER SET latin1
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

# 6. Afficher tous les titres de films de la table netflix_titles dont l’ID est inférieur strict à 80000000
SELECT title from netflix_title where show_id <  80000000;

# 7. Afficher toutes les durée des TV Show
 SELECT type, duration from netflix_title where type = "TV Show";
 
# 8. Réaliser une veille sur ces notions MySQL (https://sql.sh/fonctions/right)
	#a. Tri des données
    #b. Renommage
    #c. Agrégation
    #d. Jointures
    #e. Opération
    
# 9. Afficher tous les noms de films communs aux 2 tables (netflix_titles et netflix_shows)
SELECT netflix_title.title from netflix_title
INNER JOIN netflix_shows ON netflix_title.title = netflix_shows.title;

# 10.Calculer la durée totale de tous les TV Show de votre table netflix_titles
SELECT type,sum(duration) from netflix_title WHERE type = "Movie";

# 11. Compter le nombre de TV Shows de votre table ‘netflix_shows’ dont le ‘ratingLevel’ est renseigné.
select count(ratingLevel) from netflix_shows where ratingLevel <> "";

# 12. Compter les films et TV Shows pour lesquels les noms (title) sont les mêmes sur les 2 tables
#et dont le ‘release year’ est supérieur à 2016.

select count(netflix_title.title) from netflix_title
INNER JOIN netflix_shows ON netflix_title.title = netflix_shows.title
WHERE netflix_shows.title=netflix_title.title 
and(netflix_title.release_year > 2016 and netflix_shows.release_year >2016);

# 13. Supprimer la colonne ‘rating’ de votre table ‘netflix_shows’
ALTER TABLE netflix_shows DROP column rating;

# 14. Supprimer les 100 dernières lignes de la table ‘netflix_shows’
# il faut créer une colonne id
ALTER TABLE netflix_shows
ADD id_shows INT PRIMARY KEY NOT NULL AUTO_INCREMENT;

#supprimer les 100 dernières lignes
select id_shows
 from netflix_shows order by id_shows desc limit 200;
DELETE FROM netflix_shows ORDER BY id_shows desc limit 100;

# 15. Le champs “ratingLevel” pour le TV show “Marvel's Iron Fist” de la table ‘netflix_shows’ estvide, pouvez-vous ajouter un commentaire ?

UPDATE netflix_shows SET ratingLevel = 'Top' WHERE title = "Marvel's Iron Fist";