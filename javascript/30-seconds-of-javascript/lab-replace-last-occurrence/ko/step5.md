# 모듈 생성 및 함수 사용

이 마지막 단계에서는 함수를 다른 파일에서 가져와 사용할 수 있는 적절한 JavaScript 모듈로 변환합니다. 이는 실제 JavaScript 개발에서 흔히 사용되는 방식입니다.

먼저, 함수에 대한 모듈 파일을 만들어 보겠습니다. `replace-last` 디렉토리에 `replaceLastModule.js`라는 새 파일을 만듭니다:

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

이제 모듈을 사용하기 위해 다른 파일을 만들어 보겠습니다. `replace-last` 디렉토리에 `app.js`라는 새 파일을 만듭니다:

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

모듈이 어떻게 작동하는지 확인하기 위해 앱을 실행합니다:

```bash
node app.js
```

`replaceLast` 함수가 다양한 시나리오에서 어떻게 사용될 수 있는지 보여주는 모든 예제가 포함된 출력을 볼 수 있습니다.

축하합니다. 유용한 JavaScript 유틸리티 함수를 성공적으로 만들었고, 프로젝트에서 재사용할 수 있는 모듈로 패키징했습니다.
