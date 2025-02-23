# CSVを配列に変換する

カンマ区切り値 (CSV) 文字列を2次元配列に変換するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを開始するために `node` と入力します。
2. `Array.prototype.indexOf()` を使って最初の改行文字 (`\n`) を見つけます。
3. `omitFirstRow` が `true` に設定されている場合、最初の行 (タイトル行) を削除するために `Array.prototype.slice()` を使います。
4. `String.prototype.split()` を使って各行に対して文字列を作成します。
5. 各行の値を指定された `delimiter` を使って区切るために `String.prototype.split()` を使います。
6. 2番目の引数 `delimiter` を指定しない場合、既定の区切り文字 `','` が使用されます。
7. 3番目の引数 `omitFirstRow` を指定しない場合、CSV文字列の最初の行 (タイトル行) が含まれます。

CSVを配列に変換するコードは次のとおりです。

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

次の例を使って関数をテストできます。

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
