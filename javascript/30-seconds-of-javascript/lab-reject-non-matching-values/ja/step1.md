# 配列の値のフィルタリング

述語関数に基づいて配列をフィルタリングし、述語関数が `false` を返す値のみを返すには、次の手順に従います。

1. 述語関数 `pred` と組み合わせて `Array.prototype.filter()` を使用します。
2. フィルターメソッドは、述語関数が `false` を返す値のみを返します。
3. 一致しない値を除外するには、述語関数と配列を `reject()` 関数に渡します。

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

`reject()` 関数の使い方の例をいくつか示します。

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

これらの手順に従えば、述語関数に基づいて配列を簡単にフィルタリングし、一致しない値を除外できます。
