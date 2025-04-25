# マッピングされた配列要素の合計を計算する関数

提供された関数を使って各要素を値にマッピングすることにより、配列の合計を計算するには、`sumBy` 関数を使います。この関数は `Array.prototype.map()` を使って各要素を `fn` が返す値にマッピングします。その後、`Array.prototype.reduce()` を使って各値を累積器に加算し、累積器は `0` の値で初期化されます。

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

使用例：

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 20 を返す
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 20 を返す
```

この関数を使ってコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。
