# Creación de tablas

En SQLite, los datos se almacenan en tablas y columnas. Necesitamos crear estas antes de poder almacenar y recuperar datos. Nuestra aplicación almacenará usuarios en la tabla `user` y publicaciones en la tabla `post`.

Crea un nuevo archivo SQL `schema.sql` y agrega el siguiente código:

```sql
# flaskr/schema.sql

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```
