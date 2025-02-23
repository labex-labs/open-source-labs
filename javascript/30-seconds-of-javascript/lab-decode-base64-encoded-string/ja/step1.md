# Base64 エンコードされた文字列をデコードする

Base-64 エンコードされたデータの文字列をデコードするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 与えられた Base-64 エンコードされた文字列を持つ `Buffer` を作成します。
3. `Buffer.prototype.toString()` を使用してデコードされた文字列を返します。

以下はコードの例です。

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

この関数をテストするには、`atob('Zm9vYmFy')` を実行して、`'foobar'` が返されることを確認します。
