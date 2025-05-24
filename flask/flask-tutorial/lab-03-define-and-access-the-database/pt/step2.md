# Criando Tabelas

No SQLite, os dados são armazenados em tabelas e colunas. Precisamos criá-las antes de podermos armazenar e recuperar dados. Nossa aplicação armazenará usuários na tabela `user` e posts na tabela `post`.

Crie um novo arquivo SQL `schema.sql` e adicione o seguinte código:

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
