# 配列から一致する要素を削除する

与えられた条件に基づいて配列から特定の要素を削除するには、`remove` 関数を使うことができます。この関数は、与えられた関数が `false` を返す要素を削除することで元の配列を変更します。

`remove` 関数を使う手順は以下の通りです。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.filter()` を使って真値を返す配列要素を見つけます。
3. `Array.prototype.reduce()` を使って `Array.prototype.splice()` を使って要素を削除します。
4. コールバック関数は 3 つの引数（値、インデックス、配列）で呼び出されます。

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

`remove` 関数を使う例を以下に示します。

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

これは削除された要素を含む新しい配列を返します。
