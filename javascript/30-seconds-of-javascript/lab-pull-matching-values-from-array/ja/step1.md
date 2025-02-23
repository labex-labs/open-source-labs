# 配列から一致する値を抽出する方法

JavaScriptを使って配列から特定の値を抽出するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.filter()` と `Array.prototype.includes()` を使って、不要な値をフィルタリングし、新しい配列を作成します。
3. `Array.prototype.length` を設定して、元の配列の長さを `0` にリセットすることで、元の配列を変更します。
4. `Array.prototype.push()` を使って、抽出された値のみで元の配列を再作成します。
5. `Array.prototype.push()` を使って、削除された値を新しい配列に追跡します。

これらの手順を実装した例の関数は次のとおりです。

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

この関数を使って、配列から特定の値を削除し、削除された要素を返すことができます。

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
