# Node.js で UUID を生成する

Node.js で UUID を生成するには、以下の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) バージョン 4 に準拠した UUID を生成するために、`crypto.randomBytes()` メソッドを使用します。
3. 生成された UUID を `Number.prototype.toString()` メソッドを使用して適切な UUID（16 進数文字列）に変換します。
4. または、同様の機能を提供する [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) メソッドを使用することもできます。

以下は、Node.js で UUID を生成するためのコード スニペットの例です。

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

`UUIDGeneratorNode()` メソッドを呼び出して UUID を生成することができます。

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
