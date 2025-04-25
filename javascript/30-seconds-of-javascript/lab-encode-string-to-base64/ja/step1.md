# 文字列を Base64 にエンコードする

String オブジェクトを Base64 エンコードされた ASCII 文字列にエンコードするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを開始するために `node` と入力します。
2. 与えられた文字列を使って `Buffer` を作成し、2 進数エンコーディングを使用します。
3. `Buffer.prototype.toString()` を使って Base64 エンコードされた文字列を返します。

以下はコードの例です。

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

これで、`encodeToBase64()` 関数を使って任意の文字列を Base64 にエンコードできます。たとえば：

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
