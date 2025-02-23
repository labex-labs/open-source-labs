# JavaScript で配列の類似度を見つける方法

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。これにより、両方の配列に表示される要素の配列を見つける方法を理解できます。次の手順に従ってください。

1. `Array.prototype.includes()` メソッドを使用して、`values` に含まれていない値を判断します。
2. `Array.prototype.filter()` メソッドを使用してそれらを削除します。

配列の類似度を見つけるコードは次のとおりです。

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

次のコマンドを実行することでこのコードをテストできます。

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

これにより、出力として `[1, 2]` が返されます。
