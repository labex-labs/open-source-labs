# JavaScriptを使って配列の特定のインデックスに値を挿入する方法

JavaScriptを使って配列の特定のインデックスに値を挿入するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. 適切なインデックスと削除数 `0` を使って `Array.prototype.splice()` メソッドを使い、挿入する値を展開します。
3. `insertAt` 関数は、配列と、インデックスと、指定されたインデックスの後に挿入する1つ以上の値を受け取ります。
4. この関数は元の配列を変更し、変更された配列を返します。

以下は、動作中の `insertAt` 関数の例です。

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

上記の例では、`insertAt` 関数を使って、`myArray` 配列の2番目のインデックスの後に値 `5` を挿入し、`otherArray` 配列の1番目のインデックスの後に値 `4`、`6`、`8` を挿入しています。
