# JavaScript で文字列をインデントする関数

与えられた文字列の各行にインデントを追加するには、JavaScript の `indentString()` 関数を使うことができます。この関数には 3 つの引数があります。`str`、`count`、および `indent` です。

- `str` 引数は、インデントを追加したい文字列です。
- `count` 引数は、各行を何回インデントするかを決定します。
- `indent` 引数は省略可能で、インデントに使用する文字を表します。これを指定しない場合、デフォルト値は半角空白文字 (`' '`) です。

以下は `indentString()` 関数のコードです。

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

この関数を使用するには、必要な引数を指定して関数を呼び出します。以下はいくつかの例です。

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

最初の例では、`indentString('Lorem\nIpsum', 2)` は `'  Lorem\n  Ipsum'` を返します。これは、入力文字列の各行が半角空白文字で 2 回インデントされたことを意味します。

2 番目の例では、`indentString('Lorem\nIpsum', 2, '_')` は `'__Lorem\n__Ipsum'` を返します。これは、入力文字列の各行がアンダースコア文字 (`'_'`) で 2 回インデントされたことを意味します。
