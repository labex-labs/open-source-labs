# 文字列を埋める関数

指定された文字で文字列を両端に埋めるには、指定された `length` より短い場合、次の関数を使用します。

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

この関数は、`String.prototype.padStart()` と `String.prototype.padEnd()` を使って、与えられた文字列を両端に埋めます。3番目の引数 `char` を省略すると、空白文字を既定の埋め文字として使用できます。

以下は、`pad()` 関数の使い方のいくつかの例です。

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
