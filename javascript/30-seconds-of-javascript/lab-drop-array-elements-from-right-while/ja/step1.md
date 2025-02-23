# 関数に基づいて配列の右側から要素を削除する

特定の条件が満たされるまで配列の末尾から要素を削除するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.slice()` を使用して配列をループし、渡された `func` が `true` を返すまで配列の最後の要素を削除します。
3. 配列の残りの要素を返します。

以下は、実装例です。

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

この関数を次のように使用できます。

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
