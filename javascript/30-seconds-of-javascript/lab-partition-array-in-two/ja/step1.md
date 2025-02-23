# 関数に基づいて配列を2つに分割する方法

与えられた関数に基づいて配列を2つに分割するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.reduce()` を使って2つの配列の配列を作成します。
3. `Array.prototype.push()` を使って、`fn` が `true` を返す要素を最初の配列に追加し、`fn` が `false` を返す要素を2番目の配列に追加します。

使用できるコードは次のとおりです。

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

このコードをテストするには、次の例を使用できます。

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

これにより、2つの配列の配列が返されます。最初の配列には、与えられた関数が `true` を返すすべての要素が含まれ、2番目の配列には、与えられた関数が `false` を返すすべての要素が含まれます。
