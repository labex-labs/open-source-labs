# JavaScript でソート済み配列をマージする方法

JavaScript で 2 つのソート済み配列をマージするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. スプレッド演算子 (`...`) を使って、与えられた 2 つの配列をクローンします。
3. `Array.from()` を使って、与えられた配列に基づいて適切な長さの配列を作成します。
4. `Array.prototype.shift()` を使って、クローンされた配列から削除された要素で新しく作成された配列を埋めます。

2 つのソート済み配列をマージする例のコード スニペットは次のとおりです。

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // 出力：[1, 2, 3, 4, 5, 6]
```

上記のコードでは、`mergeSortedArrays` 関数は 2 つのソート済み配列を引数として取り、上記の手順に従ってマージされた配列を返します。例のコードの出力は `[1, 2, 3, 4, 5, 6]` です。
