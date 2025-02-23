# オブジェクトマージ関数

2 つ以上のオブジェクトをマージするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを開始するために `node` と入力します。
2. `Array.prototype.reduce()` と `Object.keys()` を組み合わせて、すべてのオブジェクトとキーを反復処理します。
3. `Object.prototype.hasOwnProperty()` と `Array.prototype.concat()` を使用して、複数のオブジェクトに存在するキーの値を追加します。
4. 2 つ以上のオブジェクトの組み合わせから新しいオブジェクトを作成するために、次のコード スニペットを使用します。

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

たとえば、次のオブジェクトを考えてみましょう。

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

これら 2 つのオブジェクトを `merge()` 関数を使用してマージすると、次の結果が得られます。

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
