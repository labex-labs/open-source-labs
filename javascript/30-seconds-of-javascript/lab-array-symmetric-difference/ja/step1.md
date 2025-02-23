# 配列の対称差

2 つの配列の対称差を見つけて重複する値も含めるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 各配列から `Set` を作成して、それぞれの一意の値を取得します。
3. それぞれの配列に対して `Array.prototype.filter()` を使用して、他の配列に含まれない値のみを残します。

以下がコードです。

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

次の例を使用して関数をテストできます。

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
