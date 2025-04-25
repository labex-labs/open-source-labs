# アクセントを削除する

この関数は文字列からアクセントを削除します。

- `String.prototype.normalize()` を使って、文字列を正規化された Unicode 形式に変換します。
- `String.prototype.replace()` を使って、与えられた Unicode 範囲内のダイアクリティカルマークを空文字列に置き換えます。

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

この関数を使用するには、ターミナル/SSH を開いて `node` と入力します。その後、文字列を引数として関数を呼び出します。

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
