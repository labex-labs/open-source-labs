# プロパティ順序に基づいてオブジェクトの配列をソートする方法

プロパティ順序に基づいてオブジェクトの配列をソートするには、次の手順を実行します。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.reduce()` を使用して、 `order` 配列からオブジェクトを作成し、値をキーとし、その元のインデックスを値とします。
3. `Array.prototype.sort()` を使用して、与えられた配列をソートし、 `prop` が空または `order` 配列に存在しない要素をスキップします。

以下は、プロパティ順序に基づいてオブジェクトの配列をソートするためのコード スニペットの例です。

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

`orderWith` 関数を使用して、プロパティ順序に基づいてオブジェクトの配列をソートできます。たとえば：

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
