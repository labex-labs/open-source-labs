# フィボナッチ数列

JavaScript でフィボナッチ数列を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、`node` と入力します。
2. `Array.from()` を使って、特定の長さの空の配列を作成し、最初の 2 つの値 (`0` と `1`) を初期化します。
3. `Array.prototype.reduce()` と `Array.prototype.concat()` を使って、最初の 2 つを除いて、最後の 2 つの値の和を使って配列に値を追加します。
4. `fibonacci()` 関数を呼び出し、数列の望ましい長さを引数として渡します。

以下がコードです。

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

これにより、n 番目の項までのフィボナッチ数列を含む配列が生成されます。
