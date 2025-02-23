# 配列を N 個のチャンクに分割する方法

配列を `n` 個の小さな配列に分割するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Math.ceil()` と `Array.prototype.length` を使って各チャンクのサイズを計算します。
3. `Array.from()` を使ってサイズ `n` の新しい配列を作成します。
4. `Array.prototype.slice()` を使って新しい配列の各要素を `size` の長さのチャンクにマッピングします。
5. 元の配列を均等に分割できない場合、最後のチャンクには残りの要素が含まれます。

次に、JavaScript の `chunkIntoN` 関数の例の実装を示します。

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

この関数を使って、配列とチャンク数を引数として渡すことで、配列を `n` 個のチャンクに分割できます。たとえば：

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
