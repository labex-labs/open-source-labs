# 配列の値を置き換えるか追加する方法

配列内の項目を置き換えるか、存在しない場合は追加するには、次の手順に従います。

1. スプレッド演算子 (`...`) を使って配列の浅いコピーを作成します。
2. `Array.prototype.findIndex()` を使って、提供された比較関数 `compFn` を満たす最初の要素のインデックスを見つけます。
3. そのような要素が見つからない場合は、`Array.prototype.push()` を使って新しい値を配列に追加します。
4. それ以外の場合は、`Array.prototype.splice()` を使って見つかったインデックスの値を新しい値で置き換えます。

この機能を実装する方法の例を以下に示します。

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

この関数をオブジェクトの配列でこのように使うことができます。

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
