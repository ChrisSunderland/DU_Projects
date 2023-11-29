-- DELETE TABLES

DROP TABLE IF EXISTS vg_sale;
DROP TABLE IF EXISTS vg_game;
DROP TABLE IF EXISTS vg_publisher;
DROP TABLE IF EXISTS vg_genre;
DROP TABLE IF EXISTS vg_platform;

-- CREATE TABLES

-- vg_publisher
CREATE TABLE vg_publisher(
	PUBLISHER_ID SMALLINT AUTO_INCREMENT,
    PUBLISHER_NAME VARCHAR(40),
    CONSTRAINT VG_PUBLISHER_PUBLISHER_ID_PK PRIMARY KEY (PUBLISHER_ID)
    );

-- vg_genre
CREATE TABLE vg_genre(
	GENRE_ID SMALLINT AUTO_INCREMENT,
    GENRE_NAME VARCHAR(15),
    CONSTRAINT VG_GENRE_GENRE_ID_PK PRIMARY KEY (GENRE_ID)
    );

-- vg_game
CREATE TABLE vg_game(
	GAME_ID SMALLINT AUTO_INCREMENT,
    GAME_NAME VARCHAR(200),
    GENRE_ID SMALLINT,
    CONSTRAINT VG_GAME_GAME_ID_PK PRIMARY KEY (GAME_ID),
	CONSTRAINT VG_GAME_GENRE_ID_FK FOREIGN KEY (GENRE_ID)
		REFERENCES vg_genre(GENRE_ID)
);

-- vg_platform
CREATE TABLE vg_platform(
	PLATFORM_ID SMALLINT AUTO_INCREMENT,
    PLATFORM_NAME VARCHAR(5),
    CONSTRAINT VG_PLATFORM_PLATFORM_ID_PK PRIMARY KEY (PLATFORM_ID)
    );

-- vg_sale
CREATE TABLE vg_sale(
	SALE_ID SMALLINT AUTO_INCREMENT,
    GAME_ID SMALLINT,
    PUBLISHER_ID SMALLINT,
    PLATFORM_ID SMALLINT,
    SALE_YEAR YEAR,
    NA_SALES DOUBLE(4,2),
	EU_SALES DOUBLE(4,2),
    JP_SALES DOUBLE(4,2),
    OTHER_SALES DOUBLE(4,2),
    CONSTRAINT VG_SALE_SALE_ID_PK PRIMARY KEY (SALE_ID),
    CONSTRAINT VG_SALE_GAME_ID_FK FOREIGN KEY (GAME_ID)
		REFERENCES vg_game(GAME_ID),
	CONSTRAINT VG_SALE_PUB_ID_FK FOREIGN KEY (PUBLISHER_ID)
		REFERENCES vg_publisher(PUBLISHER_ID),
	CONSTRAINT VG_SALE_PLATFORM_ID_FK FOREIGN KEY (PLATFORM_ID)
    REFERENCES vg_platform(PLATFORM_ID)
        );


-- DATA MIGRATION (bulk inserts with nested queries)

-- vg_publisher bulk insert
INSERT INTO vg_publisher(PUBLISHER_NAME)
(SELECT distinct(
	CASE WHEN publisher = 'N/A' THEN NULL
    ELSE publisher 
    END) FROM vg_csv);

-- vg_genre bulk insert
INSERT INTO vg_genre(GENRE_NAME)
(SELECT distinct(genre) FROM vg_csv);

-- vg_game bulk insert 
INSERT INTO vg_game(GAME_NAME, GENRE_ID)
(SELECT distinct(vg_csv.name), vg_genre.GENRE_ID 
FROM vg_csv JOIN vg_genre
	ON vg_csv.genre = vg_genre.GENRE_NAME);

-- vg_platform bulk insert
INSERT INTO vg_platform(PLATFORM_NAME)
(SELECT distinct(platform) FROM vg_csv);

-- vg_sale bulk insert
INSERT INTO vg_sale(GAME_ID, PUBLISHER_ID, PLATFORM_ID, SALE_YEAR, NA_SALES, EU_SALES, JP_SALES, OTHER_SALES)
(SELECT vg_game.GAME_ID, (CASE WHEN vg_csv.publisher = 'N/A' THEN NULL ELSE vg_publisher.PUBLISHER_ID END), vg_platform.PLATFORM_ID,
	(CASE WHEN vg_csv.year = 'N/A' THEN NULL ELSE vg_csv.year END), vg_csv.na_sales, vg_csv.eu_sales, vg_csv.jp_sales, vg_csv.other_sales
FROM vg_csv JOIN vg_platform 
	ON vg_csv.platform = vg_platform.PLATFORM_NAME
	LEFT JOIN vg_publisher 
		ON vg_csv.publisher = vg_publisher.PUBLISHER_NAME
    JOIN vg_game
		ON vg_csv.name = vg_game.GAME_NAME);


-- VIEW TABLES

SELECT * 
FROM vg_sale;

SELECT * 
FROM vg_game;

SELECT *
FROM vg_publisher;

SELECT *
FROM vg_genre;

SELECT *
FROM vg_platform;
