# 与えられた条件が満たされるまで値を生成する

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。その後、与えられた条件が満たされるまで新しい値を生成するジェネレータを作成できます。

このジェネレータを作成するには、次の手順に従います。

- `seed` 値を使用して現在の `val` を初期化します。
- `condition` 関数に現在の `val` を渡して呼び出したときに `false` を返す間、`while` ループを使用して反復処理を続けます。
- `yield` キーワードを使用して現在の `val` を返し、任意で新しいシード値 `nextSeed` を受け取ります。
- `next` 関数を使用して、現在の `val` と `nextSeed` から次の値を計算します。

以下はコードの例です。

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

適切な引数を使用してジェネレータを呼び出すことで使用できます。たとえば：

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

これは、`val` が `6` に等しくなったときに条件 `v > 5` が満たされるため、`1` から `5` までの値の配列を生成します。
