# JavaScript で二つの配列の和集合を求める方法

JavaScript で二つの配列の和集合を求めるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

2. 二つの配列の和集合は、二つの配列のいずれかに少なくとも一度存在するすべての要素を返します。

3. 二つの配列の和集合を取得するには、`a` と `b` のすべての値で `Set` を作成し、`Array.from()` メソッドを使用して配列に変換します。

これを実装する方法の例を以下に示します。

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));

console.log(union([1, 2, 3], [4, 3, 2])); // 出力：[1, 2, 3, 4]
```

上記の例では、`union()` 関数は二つの配列 `[1, 2, 3]` と `[4, 3, 2]` を引数として取り、二つの配列の和集合を配列 `[1, 2, 3, 4]` として返します。
