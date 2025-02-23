# 日付範囲生成器

与えられたステップで、指定された範囲内のすべての日付を生成するには、ターミナル/SSH で次のコードを入力して `node` を実行します。

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

これは、`while` ループを使って `start` から `end` まで反復処理する生成器を作成します。`Date` コンストラクタを使って範囲内の各日付を返し、`Date.prototype.getDate()` と `Date.prototype.setDate()` を使って `step` 日だけ増やします。

`step` の既定値を `1` にするには、3 番目の引数を省略します。

`dateRangeGenerator` を使う方法の例を次に示します。

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
