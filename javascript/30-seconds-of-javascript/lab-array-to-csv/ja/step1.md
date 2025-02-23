# 2 次元配列を CSV に変換する

2 次元配列をカンマ区切り値 (CSV) 文字列に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 提供された `区切り文字` を使用して、個々の 1 次元配列 (行) を文字列に結合するために `Array.prototype.map()` と `Array.prototype.join()` を使用します。
3. 各行を改行 (`\n`) で区切って、すべての行を CSV 文字列に結合するために `Array.prototype.join()` を使用します。
4. 既定の区切り文字 `,` を使用する場合は、2 番目の引数 `区切り文字` を省略します。

以下はコードの例です。

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

次のコード行を実行することで関数をテストできます。

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
