# JavaScript で最も高性能な関数を見つける方法

JavaScript で最も高性能な関数を見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.map()` を使用して、各値が `反復回数` 回実行した後の関数の実行にかかった合計時間である配列を生成します。
3. `performance.now()` の値の前後の差分を使用して、ミリ秒単位の高精度の合計時間を取得します。
4. `Math.min()` を使用して最小実行時間を見つけ、その最短時間のインデックスを返します。これは、最も高性能な関数のインデックスに対応します。
5. 2 番目の引数 `反復回数` を省略すると、関数はデフォルトで `10000` 回の反復を使用します。
6. 反復回数が多いほど結果が信頼性が高くなりますが、実行に時間がかかりますので、これを念頭に置いてください。

以下はコードの例です。

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

この関数を使用するには、関数の配列を最初の引数として、反復回数を 2 番目の引数（省略可能）として渡します。たとえば：

```js
mostPerformant([
  () => {
    // `false` を返す前に配列全体をループします
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // `false` を返す前にインデックス `1` に到達するだけです
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
