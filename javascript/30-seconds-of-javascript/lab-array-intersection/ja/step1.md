# 配列の共通部分を見つける

2 つの配列間の共通要素を見つけて重複を削除するには、次のコードを使用します。

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

このコードを使用するには、ターミナル/SSH を開いて `node` と入力します。その後、2 つの配列を引数として `intersection` 関数を呼び出します。例えば：

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

これにより、両方の配列に存在する要素が含まれ、重複が削除された配列が返されます。
