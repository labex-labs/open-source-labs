# 配列内の逆順の一意の値を見つける関数

与えられた比較関数に基づいて配列のすべての一意の値を右から見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.reduceRight()` と `Array.prototype.some()` を使って、比較関数 `fn` に基づいて、各値の最後の一意の出現のみを含む配列を作成します。
3. 比較関数には 2 つの引数があります。比較されている 2 つの要素の値です。
4. 関数を実装するコードは次のとおりです。

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. 関数をテストするには、次のコードを使用します。

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
