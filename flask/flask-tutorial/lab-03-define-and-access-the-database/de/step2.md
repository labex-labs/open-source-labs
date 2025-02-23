# Tabellen erstellen

In SQLite werden Daten in Tabellen und Spalten gespeichert. Wir müssen diese erstellen, bevor wir Daten speichern und abrufen können. Unsere Anwendung wird Benutzer in der Tabelle `user` und Beiträge in der Tabelle `post` speichern.

Erstellen Sie eine neue SQL-Datei `schema.sql` und fügen Sie den folgenden Code hinzu:

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
