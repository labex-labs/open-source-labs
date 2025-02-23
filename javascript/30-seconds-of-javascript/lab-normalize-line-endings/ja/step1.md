# 行末を正規化する関数

文字列の行末を正規化するには、次の関数を使用できます。

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- `String.prototype.replace()` を正規表現とともに使用して、行末を `normalized` バージョンに一致させて置き換えます。
- デフォルトでは、`normalized` バージョンは `'\r\n'` に設定されています。
- 異なる `normalized` バージョンを使用するには、それを第二引数として渡します。

以下はいくつかの例です：

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
