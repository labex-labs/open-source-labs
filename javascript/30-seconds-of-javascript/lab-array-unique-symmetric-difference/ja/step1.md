# 配列の一意の対称差関数

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。次の関数は、2 つの配列間の一意の対称差を返します。どちらの配列からも重複する値を削除します。

これを達成するには、各配列に対して `Array.prototype.filter()` と `Array.prototype.includes()` を使用して、もう一方の配列に含まれる値を削除します。結果から重複する値を削除するために `Set` を作成します。

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

次のように関数を使用します。

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
