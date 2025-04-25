# 関数の周波数の計算

1 秒間の関数の実行回数（hz/ヘルツ）を測定するには、`hz` 関数を使用します。これは、次の手順に従って行うことができます。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. イテレーションループの前後でミリ秒単位の差分を取得するために `performance.now()` を使用して、関数を `iterations` 回実行するのにかかった経過時間を計算します。
3. ミリ秒を秒に変換し、それを経過時間で割って 1 秒当たりのサイクル数を返します。
4. 100 回のイテレーションのデフォルトを使用したい場合は、2 番目の引数 `iterations` を省略します。

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

10,000 個の数値の配列の合計を計算する 2 つの関数のパフォーマンスを比較するために `hz` 関数を使用する例を以下に示します。

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

この例では、`sumReduce` は関数の実行頻度が低いため、`sumForLoop` よりも高速です。
