# 给文本添加颜色

要在控制台中打印带颜色的文本，请按以下步骤使用 `colorize()` 函数：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用模板字面量和特殊字符为字符串输出添加适当的颜色代码。
- 要添加背景颜色，请在字符串末尾包含一个重置背景颜色的特殊字符。

`colorize()` 函数创建一个包含 16 个属性的对象，包括黑色、红色、绿色、黄色、蓝色、品红色、青色和白色的颜色代码。此外，它还有用于为文本添加背景颜色的属性。

要使用 `colorize()` 函数，将你想要添加颜色的文本作为参数调用它，后跟颜色或背景颜色属性。例如，`colorize('foo').red` 将以红色字母打印 'foo'。

使用 `console.log()` 函数将带颜色的文本打印到控制台。

```js
const colorize = (...args) => ({
  black: `\x1b[30m${args.join(" ")}`,
  red: `\x1b[31m${args.join(" ")}`,
  green: `\x1b[32m${args.join(" ")}`,
  yellow: `\x1b[33m${args.join(" ")}`,
  blue: `\x1b[34m${args.join(" ")}`,
  magenta: `\x1b[35m${args.join(" ")}`,
  cyan: `\x1b[36m${args.join(" ")}`,
  white: `\x1b[37m${args.join(" ")}`,
  bgBlack: `\x1b[40m${args.join(" ")}\x1b[0m`,
  bgRed: `\x1b[41m${args.join(" ")}\x1b[0m`,
  bgGreen: `\x1b[42m${args.join(" ")}\x1b[0m`,
  bgYellow: `\x1b[43m${args.join(" ")}\x1b[0m`,
  bgBlue: `\x1b[44m${args.join(" ")}\x1b[0m`,
  bgMagenta: `\x1b[45m${args.join(" ")}\x1b[0m`,
  bgCyan: `\x1b[46m${args.join(" ")}\x1b[0m`,
  bgWhite: `\x1b[47m${args.join(" ")}\x1b[0m`
});
```

```js
console.log(colorize("foo").red); // 'foo' （红色字母）
console.log(colorize("foo", "bar").bgBlue); // 'foo bar' （蓝色背景）
console.log(colorize(colorize("foo").yellow, colorize("foo").green).bgWhite);
// 'foo bar' （第一个单词为黄色字母，第二个单词为绿色字母，两者均为白色背景）
```
