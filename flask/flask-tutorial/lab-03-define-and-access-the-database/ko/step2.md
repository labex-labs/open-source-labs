# 테이블 생성

SQLite 에서 데이터는 테이블과 열에 저장됩니다. 데이터를 저장하고 검색하기 전에 이러한 테이블과 열을 생성해야 합니다. 우리 애플리케이션은 사용자를 `user` 테이블에, 게시물을 `post` 테이블에 저장합니다.

새로운 SQL 파일 `schema.sql`을 생성하고 다음 코드를 추가합니다.

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
