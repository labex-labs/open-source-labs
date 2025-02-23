# Создание таблиц

В SQLite данные хранятся в таблицах и столбцах. Мы должны создать их, прежде чем сможем хранить и получать данные. Наше приложение будет хранить пользователей в таблице `user` и посты в таблице `post`.

Создайте новый SQL - файл `schema.sql` и добавьте следующий код:

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
