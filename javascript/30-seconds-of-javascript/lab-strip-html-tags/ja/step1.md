# 文字列からHTML/XMLタグを削除する方法

文字列からHTML/XMLタグを削除するには、正規表現を使用できます。次の手順に従ってください。

1. ターミナル/SSHを開きます
2. コーディングの練習を始めるために `node` を入力します
3. 次のコードを使用します：

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. 次の例で関数をテストします：

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

これにより、入力文字列からすべてのHTML/XMLタグが削除され、残りのテキストが返されます。
