# 互いに排他的な反復可能オブジェクトの確認

2 つの反復可能オブジェクトに共通する値がないかどうかを確認するには、`isDisjoint` 関数を使用できます。

その使い方は以下の通りです。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Set` コンストラクターを使用して、各反復可能オブジェクトから新しい `Set` オブジェクトを作成します。
3. `Array.prototype.every()` と `Set.prototype.has()` を使用して、2 つの反復可能オブジェクトに共通する値がないことを確認します。

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

以下はいくつかの例です。

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
