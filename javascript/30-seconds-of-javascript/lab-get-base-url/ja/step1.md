# ベース URL の取得

与えられた URL からベース URL を取得するには、次の手順に従います。

1. ターミナル/SSH を開きます。
2. コーディングの練習を始めるために `node` を入力します。
3. 次の JavaScript 関数を使用して、パラメータやフラグメント識別子なしで現在の URL を取得します。

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. `url` を、ベース URL を取得したい URL に置き換えます。
5. この関数は、`'?'` または `'#'` のいずれかの後にあるすべてのものを見つけた場合に削除し、ベース URL を返します。
6. 以下は例です。

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
