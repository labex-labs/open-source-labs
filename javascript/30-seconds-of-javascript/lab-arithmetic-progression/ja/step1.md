# 等差数列のコード例

コーディングを練習するには、ターミナル/SSH を開き、`node` と入力します。

ここに、等差数列にある数値の配列を作成するコード例があります。この配列は、与えられた正の整数から始まり、指定された制限まで増加します。

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

このコードを使用するには、2 つの引数：始まりの正の整数と制限を持つ関数 `arithmeticProgression` を呼び出します。たとえば：

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
