# コア関数ロジックの実装

問題を理解したので、`replaceLast` 関数のコア機能を実装しましょう。まずは文字列パターンの処理に焦点を当て、次のステップで正規表現を扱います。

パターンが文字列の場合、`lastIndexOf` メソッドを使用して最後の出現箇所の位置を見つけることができます。この位置がわかったら、`slice` メソッドを使用して置換文字列を挿入した新しい文字列を再構築できます。

`replaceLast` 関数を次の実装で更新します。

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  if (typeof pattern === "string") {
    // Find the position of the last occurrence
    const lastIndex = str.lastIndexOf(pattern);

    // If pattern not found, return original string
    if (lastIndex === -1) {
      return str;
    }

    // Rebuild the string with the replacement
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // We'll handle regex patterns in the next step
  return str;
}
```

関数が文字列パターンを正しく処理することを確認するために、テストケースを更新します。

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

更新された出力を確認するために、コードを再度実行します。

```bash
node replaceLast.js
```

これで、各テストケースで文字列パターンの最後の出現箇所が置き換えられた結果が表示されるはずです。たとえば、"Hello world world" ではなく "Hello world JavaScript" が表示されます。
