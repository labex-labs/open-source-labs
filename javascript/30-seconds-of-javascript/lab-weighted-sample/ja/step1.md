# JavaScript の配列から重み付きサンプルを取得する方法

提供された重みに基づいて配列からランダムに要素を取得するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.reduce()` を使用して、`weights` の各値に対する部分和の配列を作成します。
3. `Math.random()` を使用して乱数を生成し、`Array.prototype.findIndex()` を使用して、以前生成した配列に基づいて正しいインデックスを見つけます。
4. 最後に、生成されたインデックスを持つ `arr` の要素を返します。

これを達成するためのコードは次のとおりです。

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

この関数をテストするには、配列とその対応する重みを引数として渡します。

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
