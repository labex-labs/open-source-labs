# n 番目の引数を取得する関数

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。以下は、インデックス `n` の引数を取得する関数を作成する方法です。

- `Array.prototype.slice()` を使って、インデックス `n` の目的の引数を取得します。
- `n` が負の場合、末尾から n 番目の引数が返されます。

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

`nthArg` 関数の使い方の例を以下に示します。

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // 出力：3
console.log(third(1, 2)); // 出力：undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // 出力：5
```
