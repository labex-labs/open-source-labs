# マッピングによる 2 つの配列の差を返す関数

コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。

この関数は 2 つの配列を受け取り、両方の配列の各要素に指定された関数を適用して、それらの差を返します。

これを行うには：

- 2 番目の配列 (`b`) の各要素に関数 (`fn`) を適用することで `Set` を作成します。
- `Array.prototype.map()` を使って、1 番目の配列 (`a`) の各要素に関数 (`fn`) を適用します。
- `Set.prototype.has()` を使って、1 番目の配列 (`a`) に対して関数 (`fn`) と組み合わせて `Array.prototype.filter()` を使い、2 番目の配列 (`b`) に含まれない値のみを残します。

ここに関数のコードを示します：

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

この関数の使い方の例をいくつか示します：

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
