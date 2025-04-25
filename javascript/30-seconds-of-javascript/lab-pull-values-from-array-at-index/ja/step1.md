# インデックスの配列から値を抽出する方法

特定のインデックスの配列から特定の値を抽出するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.filter()` と `Array.prototype.includes()` を使って不要な値をフィルタリングし、`removed` と呼ばれる新しい配列に格納します。
3. `Array.prototype.length` を `0` に設定して、元の配列の長さをリセットすることで元の配列を変更します。
4. `Array.prototype.push()` を使って、抽出された値のみで元の配列を再作成します。
5. `Array.prototype.push()` を使って、削除された値を追跡します。
6. `pullAtIndex` 関数は 2 つの引数を取ります。元の配列と抽出するインデックスの配列です。
7. 関数は削除された値の配列を返します。

使用例：

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
