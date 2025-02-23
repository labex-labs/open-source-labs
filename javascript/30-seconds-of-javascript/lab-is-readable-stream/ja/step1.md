# ストリームが読み取り可能かどうかを確認する

与えられた引数が読み取り可能なストリームかどうかを確認するには、次の手順に従います。

- まず、ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
- 値が `null` でないことを確認します。
- `typeof` を使用して、値が `object` であり、`pipe` プロパティが `function` であることを確認します。
- さらに、`_read` および `_readableState` プロパティの `typeof` がそれぞれ `function` および `object` であることを確認します。

これらの手順を実装した例の関数は次のとおりです。

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

この関数を使用して、ストリームが読み取り可能かどうかを確認することができます。例えば：

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
