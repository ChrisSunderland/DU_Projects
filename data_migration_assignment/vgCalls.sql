
call gameProfitbyRegion(35, 'WD');
-- Result ==>  Wii Sports = 82.74, Super Mario Bros = 40.24, Mario Kart Wii = 35.83
call gameProfitbyRegion(12, 'EU');
-- Result ==>  Wii Sports = 29.02, Mario Kart Wii = 12.88
call gameProfitByRegion(10, 'JP');
-- Result ==>  Pokemon Red / Pokemon Blue = 10.22

call genreRankingByRegion('Sports', 'WD');
-- Result ==>  2
call genreRankingByRegion('Role-Playing', 'NA');
-- Result ==>  7
call genreRankingByRegion('Role-Playing', 'JP');
-- Result ==> 1

call publishedReleases('Electronic Arts', 'Sports');
-- Result ==> 212
call publishedReleases('Electronic Arts', 'Action');
-- Result ==> 63

call addNewRelease('Foo Attacks', 'X360', 'Strategy', 'Stevenson Studios')
-- Note ==> The Stored Procedure automatically runs selects which confirm that the data's been inserted