# 完全な toPascalCase 関数の作成

必要なすべての要素を理解したので、任意の入力文字列を処理できる完全な `toPascalCase` 関数を作成しましょう。

1. 関数を保存するための JavaScript ファイルを作成しましょう。Ctrl+C を 2 回押すか、`.exit` と入力して Node.js セッションを終了します。

2. WebIDE で、上部メニューの「File」>「New File」をクリックして新しいファイルを作成します。

3. ファイルを `/home/labex/project` ディレクトリに `pascalCase.js` として保存します。

4. 以下のコードをエディタにコピーして貼り付けます。

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Ctrl+S を押すか、メニューから「File」>「Save」を選択してファイルを保存します。

6. ターミナルを開き、以下を入力して Node.js でファイルを実行します。

```bash
node pascalCase.js
```

以下の出力が表示されるはずです。

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

私たちの `toPascalCase` 関数は正常に動作しています。その動作を見てみましょう。

1. 正規表現を使用して、使用される区切り文字に関係なく入力文字列内の単語を一致させます。
2. 単語が見つかったかどうかを確認します。見つからない場合は、空の文字列を返します。
3. `map()` を使用して各単語を大文字化し、`join('')` を使用して区切り文字なしで結合します。
4. 結果は、各単語が大文字で始まり、残りが小文字になっているパスカルケース (Pascal case) の文字列です。
