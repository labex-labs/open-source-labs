# 大文字小文字を区別しない部分文字列検索

文字列が特定の部分文字列を含んでいるかどうかを大文字小文字を区別せずに確認するには、次の手順に従います。

- `RegExp` コンストラクタに `'i'` フラグを付けて、大文字小文字を無視して指定された `searchString` と一致する正規表現を作成します。
- `RegExp.prototype.test()` を使用して、文字列が部分文字列を含んでいるかどうかを確認します。

以下はコードの例です。

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

この関数をテストするには、次のように実行できます。

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
