# 関数を使って配列から一意の値を見つける

配列のすべての一意の値を見つけるには、比較関数を提供します。

`Array.prototype.reduce()` と `Array.prototype.some()` を使って、各値の最初の一意の出現のみを含む配列を作成します。比較関数 `fn` は、比較対象の 2 つの要素の値を 2 つの引数として受け取ります。

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

この関数をテストするには、以下の例を使います：

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

ターミナル/SSH を開いて `node` と入力することでコーディングの練習を始めましょう。
