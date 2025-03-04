# JavaScript で配列要素を削除する方法

JavaScript の配列の先頭から要素を削除するには、次の手順に従います。

1. ターミナルまたは SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.slice()` メソッドを使用して、先頭から `n` 個の要素を削除した新しい配列を作成します。
3. 以下のコード スニペットの `take` 関数を使用してロジックを実装します。

```js
const take = (arr, n = 1) => arr.slice(0, n);
```

`take` 関数の使用方法の例を以下に示します。

```js
take([1, 2, 3], 5); // [1, 2, 3]
take([1, 2, 3], 0); // []
```

最初の例では、`take([1, 2, 3], 5)` は配列に要素が 3 つしかないため `[1, 2, 3]` を返します。2 番目の例では、`take([1, 2, 3], 0)` は配列の先頭から要素を取らないため `[]` を返します。
