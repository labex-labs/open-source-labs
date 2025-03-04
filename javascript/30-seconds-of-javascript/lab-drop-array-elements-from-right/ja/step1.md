# 配列の要素を右側から削除する

配列の右側から指定された数の要素を削除するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.slice()` を使って右側から指定された数の要素を削除します。
3. 1 つの要素のみを削除したい場合は、最後の引数 `n` を省略でき、デフォルト値の `1` が使用されます。

以下はコードの例です。

```js
const dropRight = (arr, n = 1) => arr.slice(0, -n);
```

この関数を以下の例でテストできます。

```js
dropRight([1, 2, 3]); // [1, 2]
dropRight([1, 2, 3], 2); // [1]
dropRight([1, 2, 3], 42); // []
```
