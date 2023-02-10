CREATE VIEW h_sum_reusable_fs_type_rocket
AS
SELECT Sum(height_meters)
FROM "Rocket"
         JOIN "RocketFirstStage"
              ON "Rocket".engines_id = "RocketFirstStage".id
WHERE reusable = true
  AND "Rocket".type = 'rocket';

CREATE VIEW avg_num_legs_type_rocket_group_material
AS
SELECT Avg("RocketLandingLegs".number) AS avg_landing_legs_number
FROM "Rocket"
         JOIN "RocketLandingLegs"
              ON "Rocket".landing_legs_id = "RocketLandingLegs".id
WHERE "Rocket".type = 'rocket'
GROUP BY "RocketLandingLegs".material;

CREATE VIEW sum_publications
AS
SELECT Sum(s)
FROM (SELECT (Count(twitter) + Count(website)
    + Count(wikipedia)) AS s
      FROM "Mission"
      UNION ALL
      SELECT Count(wikipedia) AS s
      FROM "Rocket"
      UNION ALL
      SELECT (Count(article_link) + Count(wikipedia)) AS s
      FROM "Launch"
               JOIN "LaunchLinks" LL
                    ON "Launch".links_id = LL.links_id) AS t;