# JavaScript を使って関数に基づいて配列の共通部分を見つける方法

提供された比較関数に基づいて両方の配列に存在する要素を見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

2. 提供された比較関数と組み合わせて `Array.prototype.filter()` と `Array.prototype.findIndex()` を使用して、共通する値を決定します。

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. `intersectionWith()` 関数に 2 つの配列と比較関数を引数として渡します。

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

これにより、提供された比較関数に基づいて、2 つの配列間の共通する値を含む配列が返されます。
