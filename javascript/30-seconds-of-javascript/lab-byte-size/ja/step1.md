# JavaScript で文字列のバイトサイズを取得する方法

JavaScript で文字列のバイトサイズを取得するには、以下の手順に従ってください。

1. ターミナル/SSH を開き、`node` と入力してコーディングの練習を開始します。
2. 文字列を[`Blob` オブジェクト](https://developer.mozilla.org/en-US/docs/Web/API/Blob)に変換します。
3. `Blob.size` を使用して、文字列のバイト数を取得します。

以下は、文字列のバイトサイズを取得する JavaScript コードです。

```js
const byteSize = (str) => new Blob([str]).size;
```

以下の例でこの関数をテストすることができます。

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
