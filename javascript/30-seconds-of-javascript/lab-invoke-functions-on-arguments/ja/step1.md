# 引数に対する関数の呼び出し

Node.js を使ってコードを実行するには、ターミナル/SSH を開き、`node` と入力します。

受け取った引数で各提供された関数を呼び出し、結果を返す関数を作成するには：

- `Array.prototype.map()` と `Function.prototype.apply()` を使って、各関数を与えられた引数に適用します。

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

例：

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
