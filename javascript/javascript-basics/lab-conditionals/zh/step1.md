# 条件语句

> 打开终端/SSH 并输入 `node` 开始练习编码。

条件语句是用于测试表达式是否返回 `true` 的代码结构。一种非常常见的条件语句形式是 `if...else` 语句。例如：

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

`if ()` 内部的表达式就是测试。它使用严格相等运算符（如上所述）将变量 `iceCream` 与字符串 `chocolate` 进行比较，以查看两者是否相等。如果此比较返回 `true`，则运行第一段代码。如果比较结果不为 `true`，则运行 `else` 语句之后的第二段代码。
