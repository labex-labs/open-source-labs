# 文字列の文字をマッピングする関数

この関数を使って文字列の文字をマッピングするには、次の手順に従います。

- ターミナル/SSH を開き、コーディングを練習するために `node` を入力します。
- `String.prototype.split()` と `Array.prototype.map()` を使って、与えられた文字列の各文字に対して提供された関数 `fn` を呼び出します。
- `Array.prototype.join()` を使って、文字の配列を再結合して新しい文字列を作成します。
- コールバック関数 `fn` には、3 つの引数が渡されます。現在の文字、現在の文字のインデックス、および `mapString` が呼び出された文字列。

関数のコードは次のとおりです。

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

使用例:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
