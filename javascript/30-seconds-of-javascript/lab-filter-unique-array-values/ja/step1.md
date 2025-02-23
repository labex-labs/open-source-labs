# JavaScript を使って配列内の一意の値をフィルタリングする方法

JavaScript を使って配列内の一意の値をフィルタリングするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Set` コンストラクタとスプレッド演算子 (`...`) を使って、元の配列の一意の値の配列を作成します。
3. `Array.prototype.filter()` を使って、非一意の値のみを含む配列を作成します。
4. `filterUnique` という関数を定義し、引数として配列を受け取り、上記の手順を適用します。
5. 引数として配列を使って `filterUnique` 関数を呼び出します。

これを達成するためのコードの例は次のとおりです。

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

上記のコード スニペットでは、`filterUnique` 関数は配列を受け取り、`Set` コンストラクタと `Array.prototype.filter()` メソッドを適用して、非一意の値のみを含む配列を返します。
