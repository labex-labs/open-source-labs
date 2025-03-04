# 特定のサイズのチャンクに配列を分割する方法

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

配列を指定されたサイズの小さな配列に分割するには、次の手順に従います。

1. 生成されるチャンク数に合う新しい配列を作成するために `Array.from()` を使用します。
2. 新しい配列の各要素を `size` の長さのチャンクにマッピングするために `Array.prototype.slice()` を使用します。
3. 元の配列を均等に分割できない場合、最後のチャンクには残りの要素が含まれます。

以下はコードの例です。

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

この関数を使用するには、分割したい配列とチャンクの希望するサイズを渡します。たとえば：

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
