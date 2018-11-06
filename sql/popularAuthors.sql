  SELECT author.name, count(author.name) AS Views
    FROM log l, articles a JOIN authors author ON author.id = a.author
   WHERE substring(l.path, 10) = a.slug
GROUP BY author.name
ORDER BY Views DESC
