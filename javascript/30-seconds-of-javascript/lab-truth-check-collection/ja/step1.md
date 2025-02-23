# 真偽値チェックコレクション関数

コーディングの練習のために、ターミナル/SSH で `node` を入力します。

ここに、コレクションのすべての要素に対して述語関数が真偽値を返すかどうかをチェックする関数があります。

- `Array.prototype.every()` を使用して、渡された各オブジェクトが指定されたプロパティを持ち、かつ真偽値を返すかどうかをチェックします。

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

使用例:

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
