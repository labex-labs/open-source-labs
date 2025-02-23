# 提供された関数を使って配列の最小値と最大値を求める方法

コーディングを練習するには、ターミナルまたはSSHを開いて `node` と入力します。

ここに、比較ルールを設定する提供された関数に基づいて配列の最小値と最大値を返す関数があります。

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

これを使用するには、次の手順に従います。

1. 処理したい配列とオプションの `comparator` 関数を使って `reduceWhich` を呼び出します。
2. `reduceWhich` 関数は、`Array.prototype.reduce()` を `comparator` 関数と組み合わせて使用して、配列内の適切な要素を返します。
3. 2番目の引数 (`comparator`) を省略した場合、配列の最小要素を返す既定の関数が使用されます。

以下は、`reduceWhich` を使用する方法のいくつかの例です。

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

上記の例では、最初の `reduceWhich` の呼び出しは配列 `[1, 3, 2]` の最小値である `1` を返します。2番目の呼び出しは、比較の順序を逆転させる `comparator` 関数に基づいて、同じ配列の最大値を返します。3番目の呼び出しは、オブジェクトの `age` プロパティを比較する `comparator` 関数に基づいて、`age` プロパティが最小の配列内のオブジェクトを返します。
