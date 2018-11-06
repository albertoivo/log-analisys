  SELECT a.title, count(a.title) AS quantity
    FROM log l, articles a
   WHERE substring(l.path, 10) = a.slug
GROUP BY a.title
ORDER BY quantity DESC
   LIMIT 3
