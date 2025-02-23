# 二項係数の計算

`n` 個のアイテムから重複なく順序なしで `k` 個のアイテムを選ぶ方法の数を計算するには、次の JavaScript 関数を使用できます。

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

この関数を使用するには、ターミナル/SSH を開いて `node` と入力します。その後、関数に必要な値を渡して呼び出します。たとえば：

```js
binomialCoefficient(8, 2); // 28
```

関数が正しく機能することを確認するには、次の手順に従います。

1. `Number.isNaN()` を使用して、2つの値のいずれかが `NaN` であるかどうかを確認します。
2. `k` が `0` 未満、`n` 以上、`1` または `n - 1` に等しいかどうかを確認し、適切な結果を返します。
3. `n - k` が `k` 未満であるかどうかを確認し、それに応じてそれらの値を交換します。
4. `2` から `k` までループして二項係数を計算します。
5. 計算時の丸め誤差を考慮するために `Math.round()` を使用します。
