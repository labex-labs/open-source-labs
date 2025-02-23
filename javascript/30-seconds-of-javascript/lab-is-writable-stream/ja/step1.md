# ストリームが書き込み可能かどうかを確認する

ストリームが書き込み可能かどうかを確認するには、ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。次に、以下の手順に従います。

1. 与えられた引数が `null` でないことを確認します。
2. `typeof` を使用して、値が `object` であり、`pipe` プロパティが `function` であることを確認します。
3. さらに、`_write` と `_writableState` プロパティの `typeof` がそれぞれ `function` と `object` であることを確認します。

これらのチェックを実装した例コードは以下の通りです。

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

この関数を、Node.js の `fs` モジュールを使用してテストすることができます。たとえば：

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
