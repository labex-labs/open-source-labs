# はい/いいえ文字列をチェックする関数

文字列が「はい」または「いいえ」の回答であるかどうかをチェックするには、ターミナル/SSHで`node`を入力して以下の関数を使用します。

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- 文字列が「y」/「yes」の場合、関数は`true`を返し、文字列が「n」/「no」の場合、関数は`false`を返します。
- 既定の回答を設定するには、2番目の引数`def`を省略します。既定では、関数は`false`を返します。
- 関数は、`RegExp.prototype.test()`を使用して、文字列が「y」/「yes」または「n」/「no」と一致するかどうかをチェックします。

使用例：

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
