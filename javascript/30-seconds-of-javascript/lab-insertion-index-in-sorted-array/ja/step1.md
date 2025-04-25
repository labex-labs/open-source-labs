# ソート済み配列における挿入インデックスの取得方法

ソート済み配列に値を挿入するための最も低いインデックスを見つけるには、次の手順に従います。

1. 配列が降順にソートされているかどうかを確認します。
2. `Array.prototype.findIndex()` メソッドを使用して、要素を挿入する適切なインデックスを見つけます。

これを実装するコードは次のとおりです。

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

ソート済み配列と挿入したい値を渡して `sortedIndex` 関数を呼び出すことができます。以下にいくつかの例を示します。

```js
sortedIndex([5, 3, 2, 1], 4); // 出力：1
sortedIndex([30, 50], 40); // 出力：1
```

この関数を使用することで、ソート済み配列における値の挿入インデックスを簡単に見つけることができます。
