-- Which days more than 1% of requests resulted in errors?

SELECT
  ROUND(CAST(float8(SUM("404 NOT FOUND") * 100.0 / COUNT(*)) AS numeric), 2),
  COALESCE(to_char(TIME, 'Month DD, YYYY'), '')
  FROM (SELECT
      CASE
        WHEN status <> '200 OK' THEN 1
        ELSE 0 END AS "404 NOT FOUND",
      TIME
    FROM log) AS NOTFOUND
GROUP BY COALESCE(to_char(TIME, 'Month DD, YYYY'), '')
  HAVING (SUM("404 NOT FOUND") * 100.0 / COUNT(*)) >= 1.0