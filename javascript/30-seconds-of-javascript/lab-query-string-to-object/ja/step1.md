# クエリ文字列をオブジェクトに変換する

クエリ文字列または URL をオブジェクトに変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. 与えられた`url`からパラメータを抽出するために`String.prototype.split()`を使用します。
3. `URLSearchParams`コンストラクタを使用してオブジェクトを作成し、スプレッド演算子 (`...`) を使用してキーと値のペアの配列に変換します。
4. キーと値のペアの配列をオブジェクトに変換するために`Array.prototype.reduce()`を使用します。

クエリ文字列を変換するコードは次のとおりです。

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

使用例：

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
