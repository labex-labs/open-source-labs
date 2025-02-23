# 関数に基づいて配列要素をグループ化解除する方法

`zip` によって生成された配列の要素をグループ化解除し、関数を適用する必要がある場合は、`unzipWith` を使用できます。以下はその実装方法です。

1. `Math.max()` と展開演算子 (`...`) を使用して配列内の最長のサブ配列を取得し、`Array.prototype.map()` を使用して各要素を配列にします。
2. `Array.prototype.reduce()` と `Array.prototype.forEach()` を使用して、グループ化された値を個々の配列にマッピングします。
3. `Array.prototype.map()` と展開演算子 (`...`) を使用して、`fn` を各個々の要素グループに適用します。

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

`unzipWith` を使用するには、ターミナル/SSH を開いて `node` と入力します。その後、次の例を実行できます。

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

これにより、`zip` によって生成された入力配列の要素をグループ化解除し、提供された関数を適用することで要素の配列が作成されます。
