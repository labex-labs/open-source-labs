# Création des tables

En SQLite, les données sont stockées dans des tables et des colonnes. Nous devons les créer avant de pouvoir stocker et récupérer des données. Notre application stockera les utilisateurs dans la table `user` et les publications dans la table `post`.

Créez un nouveau fichier SQL `schema.sql` et ajoutez le code suivant :

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
