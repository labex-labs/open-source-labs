# 英数字の理解

英数字は、英語のアルファベットの 26 文字（大文字 A - Z と小文字 a - z）と 10 個の数字（0 - 9）で構成されています。文字列が英数字であるかどうかをチェックするときは、その文字列がこれらの文字のみを含み、他の文字を含まないことを検証しています。

JavaScript では、正規表現を使用して英数字をチェックすることができます。正規表現（regex）は、文字列内の文字の組み合わせをマッチさせるために使用されるパターンです。

まず、コードエディタを開きましょう。WebIDE では、左側のファイルエクスプローラーに移動し、新しい JavaScript ファイルを作成します。

1. ファイルエクスプローラーパネル内で右クリックします。
2. 「New File」を選択します。
3. ファイル名を `alphanumeric.js` とします。

ファイルを作成すると、自動的にエディタで開くはずです。開かない場合は、ファイルエクスプローラーで `alphanumeric.js` をクリックして開きます。

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

次に、以下のコードを入力しましょう。

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

`Ctrl + S` を押すか、メニューから「File」>「Save」を選択してファイルを保存します。

次に、この JavaScript ファイルを実行して出力を確認しましょう。メニューから「Terminal」>「New Terminal」を選択するか、`` Ctrl + ` `` を押して WebIDE のターミナルを開きます。

ターミナルで以下のコマンドを実行します。

```bash
node alphanumeric.js
```

以下の出力が表示されるはずです。

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

この出力から、`hello123` と `123` が英数字の文字列として正しく識別され、`hello 123`（スペースを含む）と `hello@123`（特殊文字 @ を含む）は英数字ではないことがわかります。
