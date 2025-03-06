# 使用正则表达式进行单词拆分

要将字符串转换为帕斯卡命名法（Pascal case），第一步是将字符串拆分为单个单词。你可以使用正则表达式（regex）来识别单词边界，而无需考虑所使用的分隔符（空格、连字符、下划线等）。

在 JavaScript 中，正则表达式用斜杠括起来 (`/pattern/`)。下面来探讨如何使用正则表达式将字符串拆分为单词。

1. 在你的 Node.js 会话中，先尝试一个简单的示例。输入以下代码：

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

输出应该是：

```
[ 'hello', 'world', 'example' ]
```

这个正则表达式 `/[-_]/` 匹配连字符或下划线，`split()` 方法将这些匹配项用作分隔符。

2. 现在，尝试一个更复杂的字符串和正则表达式。输入：

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

输出应该是：

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

下面来拆解这个正则表达式：

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/`：匹配大写字母序列
- `/[A-Z]?[a-z]+[0-9]*/`：匹配可能以大写字母开头的单词
- `/[A-Z]/`：匹配单个大写字母
- `/[0-9]+/`：匹配数字序列
- `g` 标志使匹配具有全局性（查找所有匹配项）

`match()` 方法返回一个数组，其中包含在字符串中找到的所有匹配项。这对于帕斯卡命名法转换器至关重要，因为它几乎可以识别任何格式的单词。
