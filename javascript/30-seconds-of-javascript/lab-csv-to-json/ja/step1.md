# CSV から JSON

カンマ区切り値 (CSV) の文字列をオブジェクトの 2 次元配列に変換してコーディングの練習に使うには、ターミナル/SSH を開いて `node` と入力します。文字列の最初の行はタイトル行として使用されます。CSV を JSON に変換する手順は以下の通りです。

1. `Array.prototype.indexOf()` を使って最初の改行文字 (`\n`) を見つけます。
2. `Array.prototype.slice()` を使って最初の行（タイトル行）を削除し、`String.prototype.split()` を使って指定された `delimiter` を使って各行を値に分割します。
3. `String.prototype.split()` を使って各行に対して文字列を作成します。
4. `String.prototype.split()` を使って各行の値を指定された `delimiter` を使って分割します。
5. `Array.prototype.reduce()` を使って各行の値に対してオブジェクトを作成し、キーはタイトル行から解析されます。
6. デフォルトの区切り文字として `,` を使うために、2 番目の引数 `delimiter` を省略します。

以下がコードです。

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

この関数をテストするには、以下の例を使います。

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
