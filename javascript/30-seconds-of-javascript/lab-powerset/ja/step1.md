# JavaScript でパワーセットを生成する方法

JavaScript で与えられた数値の配列のパワーセットを生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.prototype.reduce()` メソッドと `Array.prototype.map()` メソッドを組み合わせて、要素を反復処理し、すべての組み合わせを含む配列に結合します。
3. 次のコードを実装します。

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. パワーセットを生成するには、関数 `powerset()` を呼び出し、配列を引数として渡します。たとえば：

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

これにより、与えられた配列のすべての可能な部分集合を含む配列が返されます。
