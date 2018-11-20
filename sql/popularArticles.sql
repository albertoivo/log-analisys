-- What are the three most popular articles of all time?

  SELECT a.title, count(a.title) AS quantity
    FROM log l, articles a
   WHERE l.path = '/article/' || a.slug
GROUP BY a.title
ORDER BY quantity DESC
   LIMIT 3
