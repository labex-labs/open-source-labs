# 配列の同じ内容のチェック

順序に関係なく 2 つの配列が同じ要素を含んでいるかどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開き、`node` と入力します。
2. 両方の配列の値から作成された `Set` を対象として `for...of` ループを使用します。
3. `Array.prototype.filter()` を使用して、両方の配列における各固有の値の出現回数を比較します。
4. どの要素についてもカウントが一致しない場合は `false` を返し、そうでなければ `true` を返します。

以下はそれに対応するコードです。

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

この関数をテストするには、次のコードを使用します。

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
