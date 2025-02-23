# ソート済み配列における挿入インデックスを見つける関数

配列に値を挿入し、ソート順を維持するための最も低いインデックスを見つけるには、JavaScript の `sortedIndexBy(arr, n, fn)` 関数を使用します。

この関数は、配列が降順にソートされているかどうかを緩やかに確認し、その後、反復子関数 `fn` に基づいて適切なインデックスを見つけるために `Array.prototype.findIndex()` を使用します。

以下は、`sortedIndexBy()` 関数のコードです。

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

オブジェクトの配列、挿入する値、および反復子関数を使ってこの関数を呼び出すことができます。

たとえば、`sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` は `0` を返します。これは、`{ x: 4 }` オブジェクトを `x` プロパティに基づくソート順を維持するために挿入するインデックスです。
