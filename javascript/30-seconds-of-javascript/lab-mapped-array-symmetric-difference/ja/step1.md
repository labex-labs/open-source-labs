# マッピングされた配列の対称差

コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。

この関数は、2 つの配列の各要素に提供された関数を適用した後、それらの対称差を返します。その仕組みは次の通りです。

- 各配列から `Set` を作成して、それぞれに `fn` を適用した後の一意の値を取得します。
- それぞれに対して `Array.prototype.filter()` を使って、もう一方に含まれていない値のみを残します。

ここに `symmetricDifferenceBy` 関数のコードを示します。

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

`symmetricDifferenceBy` を次のように使うことができます。

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
