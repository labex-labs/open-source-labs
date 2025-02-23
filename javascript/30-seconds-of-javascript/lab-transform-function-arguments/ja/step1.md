# 関数の引数を変換する

関数の引数を変換するには、`overArgs` 関数を使用します。この関数は、提供された関数を変換された引数で呼び出す新しい関数を作成します。

- 引数を変換するには、`Array.prototype.map()` を展開演算子 (`...`) と組み合わせて使用し、変換された引数を `fn` に渡します。

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- `overArgs` 関数をテストするには、サンプル関数と変換の配列を作成し、その後、引数を使って新しい関数を呼び出します。

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
