# 探索检查字母数字字符串的其他方法

除了使用正则表达式，还有其他方法可以检查一个字符串是否为字母数字字符串。让我们通过创建一个名为 `alternative-methods.js` 的新文件来探索其中一些方法：

1. 在文件资源管理器面板中右键单击
2. 选择“New File”
3. 将文件命名为 `alternative-methods.js`

在文件中添加以下代码：

```javascript
// Method 1: Using regular expression (our original method)
function isAlphaNumericRegex(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Method 2: Using Array.every() and checking each character
function isAlphaNumericEvery(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  return [...str].every((char) => {
    const code = char.charCodeAt(0);
    // Check if character is a digit (0-9)
    const isDigit = code >= 48 && code <= 57;
    // Check if character is a lowercase letter (a-z)
    const isLowercase = code >= 97 && code <= 122;
    // Check if character is an uppercase letter (A-Z)
    const isUppercase = code >= 65 && code <= 90;

    return isDigit || isLowercase || isUppercase;
  });
}

// Method 3: Using a combination of match() and length
function isAlphaNumericMatch(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  // Remove all alphanumeric characters and check if anything remains
  const nonAlphaNumeric = str.match(/[^a-zA-Z0-9]/g);
  return nonAlphaNumeric === null;
}

// Test strings
const testStrings = [
  "hello123",
  "HELLO123",
  "hello 123",
  "hello@123",
  "",
  "0123456789",
  "abcdefghijklmnopqrstuvwxyz"
];

// Test each method with each string
console.log("=== Testing Different Methods ===");
console.log("String\t\t\tRegex\tEvery\tMatch");
console.log("---------------------------------------------");

testStrings.forEach((str) => {
  const displayStr = str.length > 10 ? str.substring(0, 10) + "..." : str;
  const paddedStr = displayStr.padEnd(16, " ");

  const regexResult = isAlphaNumericRegex(str);
  const everyResult = isAlphaNumericEvery(str);
  const matchResult = isAlphaNumericMatch(str);

  console.log(`"${paddedStr}"\t${regexResult}\t${everyResult}\t${matchResult}`);
});

console.log("\nPerformance Comparison:");
const iterations = 1000000;
const testString = "hello123ABCxyz45";

console.time("Regex Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericRegex(testString);
}
console.timeEnd("Regex Method");

console.time("Every Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericEvery(testString);
}
console.timeEnd("Every Method");

console.time("Match Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericMatch(testString);
}
console.timeEnd("Match Method");
```

保存文件并使用以下命令运行：

```bash
node alternative-methods.js
```

输出将显示每种方法在不同测试字符串上的表现，以及这些方法之间的性能比较。正则表达式方法通常最为简洁，而且往往速度最快，但了解其他方法也很有用。

让我们来看看每种方法：

1. `isAlphaNumericRegex`：使用正则表达式来匹配仅包含字母数字的字符。
2. `isAlphaNumericEvery`：检查每个字符的 ASCII 码，以确定它是否为字母数字字符。
3. `isAlphaNumericMatch`：移除所有字母数字字符，然后检查是否还有剩余字符。

理解不同的方法能让你在解决编程问题时更具灵活性。正则表达式功能强大，但有时可能难以阅读。对于一些程序员，尤其是不熟悉正则表达式模式的人来说，其他方法可能更直观。
