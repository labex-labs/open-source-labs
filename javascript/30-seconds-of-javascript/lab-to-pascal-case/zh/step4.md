# 创建完整的 toPascalCase 函数

既然我们已经了解了所需的所有组件，接下来就创建一个完整的 `toPascalCase` 函数，它可以处理任何输入字符串。

1. 创建一个 JavaScript 文件来保存我们的函数。通过按两次 Ctrl+C 或输入 `.exit` 退出 Node.js 会话。

2. 在 WebIDE 中，通过点击顶部菜单中的 “File” > “New File” 创建一个新文件。

3. 将文件保存为 `pascalCase.js`，保存路径为 `/home/labex/project` 目录。

4. 将以下代码复制并粘贴到编辑器中：

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

5. 按 Ctrl+S 或从菜单中选择 “File” > “Save” 来保存文件。

6. 打开终端并输入以下命令，使用 Node.js 运行该文件：

```bash
node pascalCase.js
```

你应该会看到以下输出：

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

我们的 `toPascalCase` 函数现在可以正常工作了。下面回顾一下它的工作原理：

1. 我们使用正则表达式来匹配输入字符串中的单词，而不考虑所使用的分隔符。
2. 检查是否找到了任何单词。如果没有，则返回一个空字符串。
3. 使用 `map()` 方法将每个单词的首字母大写，并使用 `join('')` 方法将它们无分隔符地组合起来。
4. 最终结果是一个帕斯卡命名法（Pascal case）的字符串，其中每个单词的首字母大写，其余字母小写。
