# バイトを人間が読みやすい文字列に変換する

バイト単位の数値を人間が読みやすい文字列に変換するには、`prettyBytes()` 関数を使用します。以下に留意点をいくつか挙げます。

- この関数は、指数に基づいてアクセスされる単位の配列辞書を使用します。
- 2 番目の引数 `precision` を使用して、数値を一定の桁数に切り捨てることができます。デフォルト値は `3` です。
- 3 番目の引数 `addSpace` を使用して、数値と単位の間にスペースを追加することができます。デフォルト値は `true` です。
- この関数は、指定されたオプションと数値が負かどうかを考慮して、整形された文字列を構築して返します。

以下は `prettyBytes()` 関数のコードです。

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

以下は `prettyBytes()` 関数の使用例です。

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
