# 標準偏差

JavaScript において数値の配列の標準偏差を計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 以下に示す `standardDeviation(arr, usePopulation = false)` 関数を使用します。
3. 数値の配列を関数の最初の引数として渡します。
4. サンプル標準偏差を取得するには、2 番目の引数 `usePopulation` を省略します。母集団標準偏差を取得するには、それを `true` に設定します。

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

使用例：

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (サンプル)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (母集団)
```
