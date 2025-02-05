# 创建表

在 SQLite 中，数据存储在表和列中。在我们能够存储和检索数据之前，需要先创建这些表。我们的应用程序将把用户存储在 `user` 表中，把帖子存储在 `post` 表中。

创建一个新的 SQL 文件 `schema.sql` 并添加以下代码：

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
