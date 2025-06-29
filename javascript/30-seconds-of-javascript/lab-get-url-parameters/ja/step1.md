# URL パラメータを持つオブジェクト

現在の URL のパラメータを含むオブジェクトを作成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 適切な正規表現を使って `String.prototype.match()` を使ってすべてのキーバリューペアを抽出します。
3. `Array.prototype.reduce()` を使ってそれらをマッピングし、単一のオブジェクトに結合します。
4. 現在の URL に適用するために引数として `location.search` を渡します。

以下がコードです。

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)),
      a
    ),
    {}
  );
```

この関数を使って任意の URL を使ってそのパラメータを持つオブジェクトを取得することができます。以下はいくつかの例です。

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam', surname: 'Smith'}
```
