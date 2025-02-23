# 条件に基づいた配列要素の削除

条件に基づいて配列の要素を削除するには、ターミナル/SSH を開いて `node` と入力します。

`takeWhile` 関数は、渡された関数が `false` を返すまで配列の要素を削除し、その後削除された要素を返します。

`takeWhile` 関数を使用する手順は次のとおりです。

- `Array.prototype.entries()` を使った `for...of` ループで配列をループ処理します。
- 関数から返される値が偽であるまでループ処理します。
- `Array.prototype.slice()` を使って削除された要素を返します。
- `fn` コールバック関数は、要素の値を 1 つの引数として受け取ります。

次のコードを使って `takeWhile` 関数を実装します。

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

次は、条件に基づいて配列から要素を削除するための `takeWhile` 関数の使用例です。

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
