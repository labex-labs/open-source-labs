# ストリームが双方向であるかどうかを確認する

ストリームが双方向（読み書き可能）であるかどうかを確認するには、ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。次に、次の手順に従います。

1. 与えられた引数が `null` と異なるかどうかを確認します。
2. `typeof` を使用して、与えられた引数が `object` 型であり、`pipe` プロパティが `function` 型であるかどうかを確認します。
3. さらに、`_read`、`_write`、`_readableState`、および `_writableState` プロパティがそれぞれ `function` 型と `object` 型であるかどうかを確認します。

以下がコードです。

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

このコードを次の例を使用してテストできます。

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
