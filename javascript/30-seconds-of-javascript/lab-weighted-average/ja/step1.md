# JavaScript で加重平均を計算する方法

JavaScript で 2 つ以上の数値の加重平均を計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.reduce()` を使って値の加重和と重みの和を作成します。
3. 値の加重和を重みの和で割って加重平均を求めます。

以下は、`weightedAverage` 関数の JavaScript コードです。

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

次のように、`weightedAverage` 関数を使って数値の配列と重みの配列の加重平均を計算できます。

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
