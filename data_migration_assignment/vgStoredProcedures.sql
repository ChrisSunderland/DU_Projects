DROP PROCEDURE IF EXISTS gameProfitByRegion;
DROP PROCEDURE IF EXISTS genreRankingByRegion;
DROP PROCEDURE IF EXISTS publishedReleases;
DROP PROCEDURE IF EXISTS addNewRelease;

delimiter //

CREATE PROCEDURE gameProfitByRegion(IN MinProfit INT, IN Region CHAR(2))
BEGIN
	
    IF Region = 'JP' THEN
		SELECT GAME_NAME, JP_SALES
        FROM vg_sale JOIN vg_game
			ON vg_sale.GAME_ID = vg_game.GAME_ID
			WHERE JP_SALES > MinProfit;
    ELSEIF Region = 'NA' THEN
		SELECT GAME_NAME, NA_SALES
        FROM vg_sale JOIN vg_game
			ON vg_sale.GAME_ID = vg_game.GAME_ID
			WHERE NA_SALES > MinProfit;
    ELSEIF Region = 'EU' THEN
		SELECT GAME_NAME, EU_SALES
        FROM vg_sale JOIN vg_game
			ON vg_sale.GAME_ID = vg_game.GAME_ID
			WHERE EU_SALES > MinProfit;
    ELSE
		SELECT GAME_NAME, (NA_SALES + EU_SALES + JP_SALES + OTHER_SALES) AS GLOBAL_SALES
		FROM vg_sale JOIN vg_game
			ON vg_sale.GAME_ID = vg_game.GAME_ID
			WHERE (NA_SALES + EU_SALES + JP_SALES + OTHER_SALES) > MinProfit;
        
    END IF;

END //



CREATE PROCEDURE genreRankingByRegion (IN GenreName VARCHAR(13), IN Region CHAR(2))
BEGIN
 
		IF Region = 'JP' THEN
            WITH profit_ranking AS 
				(SELECT vg_genre.GENRE_NAME, 
					RANK() OVER (ORDER BY SUM(JP_SALES) DESC) region_standing
						FROM vg_sale JOIN vg_game ON vg_sale.GAME_ID = vg_game.GAME_ID
                        JOIN vg_genre ON vg_genre.GENRE_ID = vg_game.GENRE_ID
                        GROUP BY vg_genre.GENRE_NAME)
            SELECT region_standing FROM profit_ranking
            WHERE GENRE_NAME = GenreName;
		
		ELSEIF Region = 'NA' THEN
            WITH profit_ranking AS 
				(SELECT vg_genre.GENRE_NAME, 
					RANK() OVER (ORDER BY SUM(NA_SALES) DESC) region_standing
						FROM vg_sale JOIN vg_game ON vg_sale.GAME_ID = vg_game.GAME_ID
                        JOIN vg_genre ON vg_genre.GENRE_ID = vg_game.GENRE_ID
                        GROUP BY vg_genre.GENRE_NAME)
            SELECT region_standing FROM profit_ranking
            WHERE GENRE_NAME = GenreName;
		
		ELSEIF Region = 'EU' THEN
			WITH profit_ranking AS 
				(SELECT vg_genre.GENRE_NAME, 
					RANK() OVER (ORDER BY SUM(EU_SALES) DESC) region_standing
						FROM vg_sale JOIN vg_game ON vg_sale.GAME_ID = vg_game.GAME_ID
						JOIN vg_genre ON vg_genre.GENRE_ID = vg_game.GENRE_ID
						GROUP BY vg_genre.GENRE_NAME)
			SELECT region_standing FROM profit_ranking
			WHERE GENRE_NAME = GenreName;
		
        ELSE
			WITH profit_ranking AS 
				(SELECT vg_genre.GENRE_NAME, 
					RANK() OVER (ORDER BY SUM(JP_SALES + NA_SALES + EU_SALES + OTHER_SALES) DESC) region_standing
						FROM vg_sale JOIN vg_game ON vg_sale.GAME_ID = vg_game.GAME_ID
						JOIN vg_genre ON vg_genre.GENRE_ID = vg_game.GENRE_ID
						GROUP BY vg_genre.GENRE_NAME)
			SELECT region_standing FROM profit_ranking
			WHERE GENRE_NAME = GenreName;
			
            
        END IF;


END //


CREATE PROCEDURE publishedReleases (IN PublisherName VARCHAR(40), IN GenreName VARCHAR(15))
BEGIN

	SELECT count(distinct(vg_game.GAME_ID)) AS TOTAL_GENRE_RELEASES
    FROM vg_sale JOIN vg_publisher
		ON vg_sale.PUBLISHER_ID = vg_publisher.PUBLISHER_ID
        JOIN vg_game 
        ON vg_sale.GAME_ID = vg_game.GAME_ID
        JOIN vg_genre
        ON vg_game.GENRE_ID = vg_genre.GENRE_ID
        WHERE PUBLISHER_NAME = PublisherName AND GENRE_NAME = GenreName;

END //


CREATE PROCEDURE addNewRelease (IN GameTitle VARCHAR(200), IN PlatformName VARCHAR(5), IN GenreName VARCHAR(15), IN PublisherName VARCHAR(40))
BEGIN

    -- add to vg_publisher (potentially)
    IF (SELECT PUBLISHER_NAME FROM vg_publisher WHERE PUBLISHER_NAME = PublisherName) IS NULL THEN
		INSERT INTO vg_publisher VALUES (null, PublisherName);
	END IF;
        
    -- add to vg_platform if provided platform isn't found
	IF (SELECT PLATFORM_NAME FROM vg_platform WHERE PLATFORM_NAME = PlatformName) IS NULL THEN
		INSERT INTO vg_platform VALUES (null, PlatformName);
	END IF;
	
	-- add to vg_genre if provided value isn't found
	IF (SELECT GENRE_NAME FROM vg_genre WHERE GENRE_NAME = GenreName) IS NULL THEN
		INSERT INTO vg_genre VALUES (null, GenreName);
	END IF;

	-- add to vg_game if provided game title isn't found    
    IF (SELECT GAME_NAME FROM vg_game WHERE GAME_NAME = GameTitle) IS NULL THEN
		INSERT INTO vg_game VALUES 
			(null, 
            GameTitle, 
            (SELECT GENRE_ID FROM vg_genre WHERE GENRE_NAME = GenreName));
	END IF;
    
    -- add to vg_sale table
    INSERT INTO vg_sale (GAME_ID, PUBLISHER_ID, PLATFORM_ID)
    VALUES 
		((SELECT GAME_ID FROM vg_game WHERE GAME_NAME = GameTitle), 
        (SELECT PUBLISHER_ID FROM vg_publisher WHERE PUBLISHER_NAME = PublisherName),
        (SELECT PLATFORM_ID FROM vg_platform WHERE PLATFORM_NAME = PlatformName));
    
    -- check that all provided values are now present in the tables
	SELECT * FROM vg_publisher WHERE PUBLISHER_NAME = PublisherName;
	SELECT * FROM vg_platform WHERE PLATFORM_NAME = PlatformName;
    SELECT * FROM vg_genre WHERE GENRE_NAME = GenreName;
    SELECT * FROM vg_game WHERE GAME_NAME = GameTitle;
	SELECT * FROM vg_sale WHERE GAME_ID = (SELECT GAME_ID FROM vg_game WHERE GAME_NAME = GameTitle);
    
END //


delimiter ;


