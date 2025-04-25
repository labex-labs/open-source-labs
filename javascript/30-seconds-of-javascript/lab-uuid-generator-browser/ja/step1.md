# ブラウザで UUID を生成する

ブラウザで[RFC4122](https://www.ietf.org/rfc/rfc4122.txt)バージョン 4 に準拠する UUID を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、`node`と入力します。
2. `Crypto.getRandomValues()`メソッドを使って UUID を生成します。
3. `Number.prototype.toString()`メソッドを使って UUID を 16 進数文字列に変換します。
4. 次のコードを実装します。

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. `UUIDGeneratorBrowser()`関数を呼び出して UUID を生成します。たとえば、`UUIDGeneratorBrowser()`は`'7982fcfe-5721-4632-bede-6000885be57d'`を返します。
