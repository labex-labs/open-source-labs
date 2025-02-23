# 条件とキーによるオブジェクトのフィルタリング

条件に基づいてオブジェクトの配列をフィルタリングすると同時に、不明なキーも除外するには、`reducedFilter()` 関数を使用します。

以下が手順です：

1. `Array.prototype.filter()` を使用して、述語 `fn` に基づいて配列をフィルタリングし、条件が真値を返したオブジェクトを返します。

2. フィルタリングされた配列に `Array.prototype.map()` を使用して新しいオブジェクトを返します。

3. `Array.prototype.reduce()` を使用して、`keys` 引数として提供されなかったキーを除外します。

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

以下は、`reducedFilter()` 関数の使用例です：

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// 出力: [{ id: 2, name:'mike'}]
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
