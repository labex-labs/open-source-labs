# オブジェクトをMapに変換する方法

オブジェクトを `Map` に変換するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
2. `Object.entries()` を使用して、オブジェクトをキーと値のペアの配列に変換します。
3. `Map` コンストラクタを使用して、配列を `Map` に変換します。

以下はコードの例です。

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

オブジェクトを `Map` に変換するには、`objectToMap()` 関数を使用できます。たとえば：

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
