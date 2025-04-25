# 特定の範囲でランダムな整数配列を生成する

特定の範囲内でランダムな整数の配列を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.from()` を使用して、必要な長さの空の配列を作成します。
3. `Math.random()` を使用してランダムな数を生成し、指定された範囲にマップします。整数に変換するには `Math.floor()` を使用します。
4. `randomIntArrayInRange()` 関数は 3 つの引数をとります。`min`、`max`、およびオプションの引数 `n`（デフォルト値は 1）です。
5. 必要な `min`、`max`、および `n` の値を使って `randomIntArrayInRange()` 関数を呼び出して、ランダムな整数配列を生成します。

コードは次のとおりです。

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

使用例：

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
