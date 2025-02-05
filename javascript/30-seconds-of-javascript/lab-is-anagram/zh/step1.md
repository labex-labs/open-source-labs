# 用于检查字符串是否为变位词的 JavaScript 函数

要检查一个字符串是否是另一个字符串的变位词，请使用以下 JavaScript 函数。它不区分大小写，并且会忽略空格、标点符号和特殊字符。

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

要使用此函数，请打开终端/SSH 并输入 `node`。然后，使用两个字符串作为参数调用该函数：

```js
isAnagram("iceman", "cinema"); // true
```

该函数使用 `String.prototype.toLowerCase()` 和 `String.prototype.replace()` 以及适当的正则表达式来删除不必要的字符。它还对两个字符串都使用了 `String.prototype.split()`、`Array.prototype.sort()` 和 `Array.prototype.join()` 来规范化它们，并检查它们的规范化形式是否相等。
