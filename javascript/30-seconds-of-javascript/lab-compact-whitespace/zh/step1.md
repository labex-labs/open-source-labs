# 压缩字符串中空白字符的函数

要压缩字符串中的空白字符，请使用 `compactWhitespace()` 函数。

- 它使用 `String.prototype.replace()` 和正则表达式，将所有两个或更多连续的空白字符替换为单个空格。
- 该函数接受一个字符串作为参数，并返回压缩后的字符串。

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

示例用法：

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
