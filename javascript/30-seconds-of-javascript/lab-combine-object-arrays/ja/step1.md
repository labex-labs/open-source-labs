# 指定されたキーに基づいてオブジェクト配列を結合する関数

特定のキーに基づいて 2 つのオブジェクト配列を結合するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 与えられた `prop` に基づいて、オブジェクトのアキュムレータを持つ `Array.prototype.reduce()` を使用して、両方の配列のすべてのオブジェクトを結合します。
3. `Object.values()` を使用して、結果のオブジェクトを配列に変換して返します。

次の関数を使用できます。

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

この関数の使用例は次のとおりです。

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
