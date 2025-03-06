# モジュールの作成と関数の使用

この最後のステップでは、関数を適切な JavaScript モジュールに変換し、他のファイルでインポートして使用できるようにします。これは、実際の JavaScript 開発で一般的な手法です。

まず、関数用のモジュールファイルを作成しましょう。`replace-last` ディレクトリに `replaceLastModule.js` という新しいファイルを作成します。

```javascript
/**
 * Replaces the last occurrence of a pattern in a string.
 *
 * @param {string} str - The input string.
 * @param {string|RegExp} pattern - The pattern to replace (string or RegExp).
 * @param {string} replacement - The replacement string.
 * @returns {string} - The string with the last occurrence replaced.
 */
function replaceLast(str, pattern, replacement) {
  // Ensure str is a string
  if (typeof str !== "string") {
    return str;
  }

  // If str is empty or pattern is not provided, return original string
  if (str === "" || pattern === undefined) {
    return str;
  }

  // Ensure replacement is a string
  if (replacement === undefined) {
    replacement = "";
  } else if (typeof replacement !== "string") {
    replacement = String(replacement);
  }

  // Handle string patterns
  if (typeof pattern === "string") {
    const lastIndex = str.lastIndexOf(pattern);
    if (lastIndex === -1) {
      return str;
    }
    return (
      str.slice(0, lastIndex) +
      replacement +
      str.slice(lastIndex + pattern.length)
    );
  }

  // Handle regular expression patterns
  if (pattern instanceof RegExp) {
    // Create a global version of the regex to find all matches
    const globalRegex = new RegExp(
      pattern.source,
      "g" + (pattern.ignoreCase ? "i" : "") + (pattern.multiline ? "m" : "")
    );

    // Find all matches
    const matches = str.match(globalRegex);

    // If no matches, return original string
    if (!matches || matches.length === 0) {
      return str;
    }

    // Get the last match
    const lastMatch = matches[matches.length - 1];

    // Find the position of the last match
    const lastIndex = str.lastIndexOf(lastMatch);

    // Rebuild the string with the replacement
    return (
      str.slice(0, lastIndex) +
      replacement +
      str.slice(lastIndex + lastMatch.length)
    );
  }

  // If pattern is neither string nor RegExp, return original string
  return str;
}

// Export the function
module.exports = replaceLast;
```

次に、このモジュールを使用する別のファイルを作成しましょう。`replace-last` ディレクトリに `app.js` という新しいファイルを作成します。

```javascript
// Import the replaceLast function
const replaceLast = require("./replaceLastModule");

// Examples of using the replaceLast function
console.log(
  "Example 1:",
  replaceLast("Hello world world", "world", "JavaScript")
);
console.log("Example 2:", replaceLast("abcabcabc", "abc", "123"));
console.log("Example 3:", replaceLast("file.txt.backup.txt", ".txt", ".md"));
console.log("Example 4:", replaceLast("123 456 789", /\d+/, "numbers"));
console.log(
  "Example 5:",
  replaceLast("The fox jumped over the lazy dog", /[a-z]+/i, "cat")
);

// Practical examples
const filePath = "/path/to/my/file.txt";
console.log("File with new extension:", replaceLast(filePath, ".txt", ".md"));

const url = "https://example.com/products/category/item?color=red";
console.log("URL with updated parameter:", replaceLast(url, "red", "blue"));

const htmlTag = "<div class='container'><p>Text</p></div>";
console.log(
  "HTML with replaced tag:",
  replaceLast(htmlTag, /<\/?\w+>/g, "<span>")
);
```

モジュールがどのように動作するかを確認するために、アプリを実行します。

```bash
node app.js
```

`replaceLast` 関数がさまざまなシナリオでどのように使用できるかを示すすべての例の出力が表示されるはずです。

おめでとうございます。便利な JavaScript ユーティリティ関数を作成し、プロジェクト全体で再利用できるモジュールとしてパッケージ化することに成功しました。
