# JavaScript で配列の末尾から要素を削除する方法

JavaScript の配列の末尾から要素を削除するには、`Array.prototype.slice()` メソッドを使用できます。以下のように行うことができます。

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

この関数は、元の配列の最後の `n` 個の要素で新しい配列を作成します。以下のように使用できます。

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

この関数を使用するには、ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
