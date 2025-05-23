# 反復可能オブジェクトのサブセットが別の反復可能オブジェクトに含まれているかどうかを確認する

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。この関数は、重複する値を除外して、最初の反復可能オブジェクトが 2 番目の反復可能オブジェクトのサブセットであるかどうかを確認します。

これを達成するには、次のことができます。

- `Set` コンストラクタを使って、各反復可能オブジェクトから新しい `Set` オブジェクトを作成します。
- `Array.prototype.every()` と `Set.prototype.has()` を使って、最初の反復可能オブジェクトのすべての値が 2 番目の反復可能オブジェクトに含まれているかどうかを確認します。

以下はサンプルの実装です。

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

2 つのセットを渡して比較することで `subSet` 関数を使うことができます。たとえば：

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
