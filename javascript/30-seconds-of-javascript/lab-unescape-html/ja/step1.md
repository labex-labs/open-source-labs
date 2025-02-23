# HTML のデエスケープ

この関数は、エスケープされた HTML 文字をデエスケープします。これを使用するには、次の手順に従ってください。

1. ターミナル/SSH を開きます。
2. `node` と入力します。
3. 次のコードをコピーして貼り付けます。

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"'
      })[tag] || tag
  );
```

4. `unescapeHTML` 関数を呼び出し、エスケープされた文字を含む文字列を渡します。
5. 関数はデエスケープされた文字列を返します。

使用例:

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
