# 用于去除空白字符的函数

要从字符串中去除空白字符，请使用以下函数。

- 使用 `String.prototype.replace()` 和正则表达式，将所有空白字符替换为空字符串。

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## 正则表达式解释

- `/\s+/g` 分解如下：
  - `\s`：匹配任何空白字符（空格、制表符、换行符）
  - `+`：匹配前一个字符的一次或多次出现
  - `/g`：全局标志 - 匹配字符串中的所有出现，而不仅仅是第一个

## 快速正则表达式参考

常见的空白字符模式：

- `\s` - 匹配任何空白字符（空格、制表符、换行符）
- `\t` - 匹配制表符
- `\n` - 匹配换行符
- `\r` - 匹配回车符
- （空格） - 仅匹配空格字符

例如：

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// 更多示例：
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
