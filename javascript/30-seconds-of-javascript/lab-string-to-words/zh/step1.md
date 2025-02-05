# 将字符串转换为单词数组的函数

要将给定的字符串转换为单词数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.split()` 方法并提供一个 `pattern`（默认为非字母字符作为正则表达式）来转换为字符串数组。
3. 使用 `Array.prototype.filter()` 方法移除任何空字符串。
4. 省略第二个参数 `pattern` 以使用默认的正则表达式。

以下是一个实现这些步骤的函数：

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

你可以使用 `words()` 函数处理不同的字符串，将它们转换为单词数组：

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
