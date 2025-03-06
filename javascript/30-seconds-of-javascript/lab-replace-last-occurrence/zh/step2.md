# 实现核心函数逻辑

既然我们已经理解了问题，接下来让我们实现 `replaceLast` 函数的核心功能。我们将首先专注于处理字符串模式，然后在下一步处理正则表达式。

当模式是一个字符串时，我们可以使用 `lastIndexOf` 方法来查找模式最后一次出现的位置。一旦知道了这个位置，我们就可以使用 `slice` 方法来重新构建字符串，并插入替换内容。

使用以下实现更新你的 `replaceLast` 函数：

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

更新你的测试用例，以检查函数是否能正确处理字符串模式：

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

再次运行代码，查看更新后的输出：

```bash
node replaceLast.js
```

现在，你应该会看到在每个测试用例中，字符串模式的最后一次出现都被替换了。例如，输出的是 "Hello world JavaScript" 而不是 "Hello world world"。
