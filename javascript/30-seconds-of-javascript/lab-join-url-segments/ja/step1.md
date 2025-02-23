# URL セグメントの結合と正規化

与えられた URL セグメントを結合し、結果の URL を正規化するには、以下の手順に従います。

1. `Array.prototype.join()` を使って URL セグメントを結合します。
2. 結果の URL を正規化するために、さまざまな正規表現を使った一連の `String.prototype.replace()` 呼び出しを行います。
   - 二重スラッシュを削除する
   - プロトコルに適切なスラッシュを追加する
   - パラメータの前のスラッシュを削除する
   - パラメータを `'&'` で結合し、最初のパラメータ区切り文字を正規化する

以下のコード スニペットを使って URL セグメントを結合して正規化します。

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

使用例:

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
