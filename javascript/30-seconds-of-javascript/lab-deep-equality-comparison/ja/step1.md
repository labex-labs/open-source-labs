# JavaScript でオブジェクトの等価性を確認する方法

2 つの値が等価であるかどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `equals()` 関数を使用して 2 つの値の間で深い比較を行います。
3. 2 つの値が同一であるかどうかを確認します。その場合は、`true` を返します。
4. `Date.prototype.getTime()` を使用して、両方の値が同じ時刻の `Date` オブジェクトであるかどうかを確認します。その場合は、`true` を返します。
5. 両方の値が等価な値を持つ非オブジェクト値であるかどうかを確認します（厳密な比較）。その場合は、`true` を返します。
6. 一方の値のみが `null` または `undefined` であるか、またはそれらのプロトタイプが異なるかどうかを確認します。その場合は、`false` を返します。
7. 上記の条件のいずれも満たされない場合、`Object.keys()` を使用して両方の値が同じ数のキーを持つかどうかを確認します。
8. `Array.prototype.every()` を使用して、`a` のすべてのキーが `b` に存在するかどうかを確認し、再帰的に `equals()` を呼び出すことでそれらが等価であるかどうかを確認します。

`equals()` 関数を実装するには、次のコードを使用します。

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

`equals()` 関数をテストするには、次のコード例を使用します。

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
