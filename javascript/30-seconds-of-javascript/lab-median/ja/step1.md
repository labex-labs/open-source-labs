# 数値の配列の中央値を計算する方法

数値の配列の中央値を計算するには、次の手順に従います。

1. 配列の中央を見つけます。
2. `Array.prototype.sort()` を使用して値をソートします。
3. `Array.prototype.length` が奇数の場合、中点の数値を返します。偶数の場合、真ん中の 2 つの数値の平均を返します。
4. コーディングを練習して `node` を使用するには、ターミナル/SSH を開き、`node` と入力します。

このロジックを実装したコードのサンプルは次のとおりです。

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

この関数を次のように数値の配列で呼び出すことができます。

```js
median([5, 6, 50, 1, -5]); // 5
```
