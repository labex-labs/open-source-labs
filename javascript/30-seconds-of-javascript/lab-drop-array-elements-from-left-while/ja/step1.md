# 関数に基づく配列要素の削除

配列から特定の要素を削除するには、`dropWhile` 関数を使用します。この関数は、渡された関数が `true` を返すまで要素を削除します。その後、関数は配列の残りの要素を返します。

動作の仕方は以下の通りです。

- `Array.prototype.slice()` を使って配列をループ処理し、`func` から返される値が `true` になるまで配列の最初の要素を削除します。
- 残りの要素を返します。

使用例：

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
