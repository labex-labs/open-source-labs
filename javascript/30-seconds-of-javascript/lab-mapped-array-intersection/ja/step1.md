# マッピングされた配列の共通部分を見つけるための手順

両方の配列の各要素に関数を適用した後、2 つの配列の共通要素を見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、`node` と入力します。
2. 以下に示すコードを使用します。

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. コード内の `a` と `b` を自分の配列に置き換え、`fn` を各要素に適用したい関数に置き換えます。
4. コードを実行して、共通要素を含む結果の配列を取得します。

例:

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

最初の例では、関数 `Math.floor` が配列 `[2.1, 1.2]` と `[2.3, 3.4]` に適用され、共通要素 `[2.1]` が返されます。
2 番目の例では、関数 `x => x.title` が配列 `[{ title: 'Apple' }, { title: 'Orange' }]` と `[{ title: 'Orange' }, { title: 'Melon' }]` に適用され、共通要素 `[{ title: 'Orange' }]` が返されます。
