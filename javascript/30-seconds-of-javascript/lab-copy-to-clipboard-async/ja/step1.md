# 文字列をクリップボードにコピーする関数

文字列をクリップボードにコピーするには、`copyToClipboardAsync` 関数を使用します。この関数は、クリップボードの内容が更新されたときに解決するプロミスを返します。手順は以下の通りです。

1. `Navigator`、`Navigator.clipboard`、および `Navigator.clipboard.writeText` が真であるかどうかを `if` 文を使用して検証することで、クリップボード API が利用可能かどうかを確認します。
2. クリップボード API が利用可能な場合、`Clipboard.writeText()` を使用して、与えられた値 `str` をクリップボードに書き込みます。
3. `Clipboard.writeText()` の結果を返します。これは、クリップボードの内容が更新されたときに解決するプロミスです。
4. クリップボード API が利用可能でない場合、`Promise.reject()` を使用して適切なエラー メッセージでプロミスを拒否します。
5. 古いブラウザをサポートする必要がある場合は、`Clipboard.writeText()` の代わりに `Document.execCommand()` を使用します。`copyToClipboard` スニペットでそれに関する詳細を確認できます。

以下が `copyToClipboardAsync` 関数です。

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

この関数を使用するには、コピーしたい文字列を引数として `copyToClipboardAsync` を呼び出します。例えば、以下のようになります。

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' がクリップボードにコピーされます。
```
