# ベースURLの取得

与えられたURLからベースURLを取得するには、次の手順に従います。

1. ターミナル/SSHを開きます。
2. コーディングの練習を始めるために `node` を入力します。
3. 次のJavaScript関数を使用して、パラメータやフラグメント識別子なしで現在のURLを取得します。

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. `url` を、ベースURLを取得したいURLに置き換えます。
5. この関数は、`'?'` または `'#'` のいずれかの後にあるすべてのものを見つけた場合に削除し、ベースURLを返します。
6. 以下は例です。

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
