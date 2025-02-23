# JavaScript を使って配列の要素をグループ化してカウントする方法

JavaScript を使って配列の要素をグループ化してカウントするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.map()` メソッドを使って、配列の値を関数またはプロパティ名にマッピングします。
3. `Array.prototype.reduce()` メソッドを使って、キーがマッピング結果から生成されるオブジェクトを作成します。
4. `countBy` という名前の関数を作成し、配列と関数を引数とします。
5. `countBy` 関数の中で、渡された引数が関数かプロパティ名かを三項演算子でチェックします。関数の場合は、マッピング関数として使います。プロパティ名の場合は、配列要素のそのプロパティにアクセスします。
6. `reduce()` メソッドを使って、各キーが配列の一意の要素を表し、その値が配列内で出現する回数であるオブジェクトを作成します。

以下がコードです。

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

次の例で `countBy` 関数をテストできます。

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
