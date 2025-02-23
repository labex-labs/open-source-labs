# 引数の結合の使用

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。引数の結合は、引数のリストで最初に定義された非 null の引数を返すために使用される技術です。これを達成するには、`Array.prototype.find()` と `Array.prototype.includes()` を使って、`undefined` または `null` と等しくない最初の値を見つけます。

以下は、JavaScript で引数の結合を使用する方法の例です。

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

上記のコード スニペットでは、`coalesce` は任意の数の引数を受け取り、最初に定義された非 null の引数を返す関数です。`coalesce` 関数を使用する方法の例を以下に示します。

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

この例では、`coalesce` に `null`、`undefined`、空文字列 `''`、`NaN`、そして文字列 `'Waldo'` を含む引数のリストが渡されます。関数は空文字列 `''` を返します。なぜなら、それがリスト内の最初に定義された非 null の引数だからです。
