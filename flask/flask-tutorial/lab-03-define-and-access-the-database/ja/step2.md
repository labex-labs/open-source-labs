# テーブルの作成

SQLite では、データはテーブルと列に格納されます。データを保存および取得する前に、これらを作成する必要があります。私たちのアプリケーションは、`user` テーブルにユーザーを保存し、`post` テーブルに投稿を保存します。

新しい SQL ファイル `schema.sql` を作成し、次のコードを追加します。

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
