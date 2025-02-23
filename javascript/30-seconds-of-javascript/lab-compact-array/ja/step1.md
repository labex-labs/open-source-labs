# コンパクトな配列を作成するための Array.prototype.filter() の使い方

JavaScript でコンパクトな配列を作成するには、`Array.prototype.filter()` メソッドを使って配列から偽の値を削除することができます。偽の値には `false`、`null`、`0`、`""`、`undefined`、`NaN` が含まれます。

以下は、`Array.prototype.filter()` を使ってコンパクトな配列を作成する方法を示すコード スニペットです。

```js
const compact = (arr) => arr.filter(Boolean);
```

その後、`compact` 関数を使って配列を引数として渡すことでコンパクトな配列を作成できます。たとえば：

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// 出力: [ 1, 2, 3, 'a','s', 34 ]
```

このように `Array.prototype.filter()` を使うことで、真の値のみを含むコンパクトな配列を簡単に作成できます。
