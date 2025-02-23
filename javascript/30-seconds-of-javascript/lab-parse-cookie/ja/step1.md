# HTTP クッキーを解析する JavaScript 関数

JavaScript で HTTP クッキーヘッダ文字列を解析し、すべてのクッキー名と値のペアのオブジェクトを返すには、次の手順に従います。

- ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
- `String.prototype.split()` を使用して、キーと値のペアを互いに分離します。
- `Array.prototype.map()` と `String.prototype.split()` を使用して、各ペアのキーと値を分離します。
- `Array.prototype.reduce()` と `decodeURIComponent()` を使用して、すべてのキーと値のペアを持つオブジェクトを作成します。

上記の手順を実装した `parseCookie()` 関数の例を以下に示します。

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

この関数を次のようにテストできます。

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
