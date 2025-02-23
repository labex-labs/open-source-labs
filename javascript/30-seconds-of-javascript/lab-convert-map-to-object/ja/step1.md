# JavaScript で Map をオブジェクトに変換する方法

JavaScript の `Map` をオブジェクトに変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Map.prototype.entries()` メソッドを使って `Map` をキーと値のペアの配列に変換します。
3. `Object.fromEntries()` メソッドを使って配列をオブジェクトに変換します。

以下は、`Map` をオブジェクトに変換するためのコード スニペットの例です。

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

関数をテストするには、次のコードを実行できます。

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
