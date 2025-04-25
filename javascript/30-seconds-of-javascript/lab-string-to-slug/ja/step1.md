# 文字列を URL スラッグに変換する関数

URL で使用できるスラッグに文字列を変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `String.prototype.toLowerCase()` と `String.prototype.trim()` メソッドを使用して文字列を正規化します。
3. `String.prototype.replace()` メソッドを使用して、スペース、ダッシュ、アンダースコアを `-` に置き換え、特殊文字を削除します。
4. 次のコードを実装します。

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. 関数を `slugify('Hello World!');` の入力でテストし、出力 `'hello-world'` が返されることを確認します。
