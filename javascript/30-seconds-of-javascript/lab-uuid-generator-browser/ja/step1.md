# ブラウザでUUIDを生成する

ブラウザで[RFC4122](https://www.ietf.org/rfc/rfc4122.txt)バージョン4に準拠するUUIDを生成するには、次の手順に従います。

1. ターミナル/SSHを開き、`node`と入力します。
2. `Crypto.getRandomValues()`メソッドを使ってUUIDを生成します。
3. `Number.prototype.toString()`メソッドを使ってUUIDを16進数文字列に変換します。
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

5. `UUIDGeneratorBrowser()`関数を呼び出してUUIDを生成します。たとえば、`UUIDGeneratorBrowser()`は`'7982fcfe-5721-4632-bede-6000885be57d'`を返します。
