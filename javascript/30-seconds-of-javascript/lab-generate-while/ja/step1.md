# 条件が真の間に値を生成するジェネレータ

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。これにより、与えられた条件が満たされている限り新しい値を生成し続けるジェネレータが作成されます。

ジェネレータは、現在の `val` を初期化するために使用される `seed` 値で初期化されます。その後、`while` ループを使用して、現在の `val` を引数に呼び出された `condition` 関数が `true` を返す間、反復処理を行います。

`yield` キーワードは、現在の `val` を返し、任意で新しいシード値 `nextSeed` を受け取ります。`next` 関数は、現在の `val` と `nextSeed` から次の値を計算するために使用されます。

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

ジェネレータを使用するには、`seed`、`condition`、および `next` 関数を使って呼び出します。たとえば、`[...generateWhile(1, v => v <= 5, v => ++v)]` を呼び出すと `[1, 2, 3, 4, 5]` が返されます。
