# Node.js で値がストリームかどうかを確認する方法

Node.js で値がストリームかどうかを確認するには、`isStream` 関数を使用できます。この関数を使用するには、次の手順に従います。

1. ターミナル/SSH を開きます。
2. コーディングの練習を始めるために `node` と入力します。
3. 与えられた引数がストリームかどうかを確認するために `isStream` 関数を使用します。
4. 値が `null` と異なるかどうかを確認するには、次のコードを使用します。

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. ファイルがストリームかどうかを確認するには、次のコードを使用します。

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
