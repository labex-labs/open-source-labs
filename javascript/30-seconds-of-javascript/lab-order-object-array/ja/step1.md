# JavaScript でオブジェクトの配列をソートする方法

JavaScript でオブジェクトの配列をソートするには、`props` 配列に対してデフォルト値 `0` で `Array.prototype.sort()` メソッドと `Array.prototype.reduce()` メソッドを使用できます。

以下は、指定されたプロパティと順序に基づいてオブジェクトの配列をソートする `orderBy` という例の関数です。

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

この関数を使用するには、オブジェクトの配列、ソート対象のプロパティの配列、および任意の順序の配列を渡します。`orders` 配列が提供されない場合、関数は既定で `'asc'` でソートします。

以下は、`orderBy` 関数の使用方法のいくつかの例です。

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// 名前で昇順、年齢で降順にソート
orderBy(users, ["name", "age"], ["asc", "desc"]);
// 出力: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// 名前で昇順、年齢で昇順（既定の順序）にソート
orderBy(users, ["name", "age"]);
// 出力: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
