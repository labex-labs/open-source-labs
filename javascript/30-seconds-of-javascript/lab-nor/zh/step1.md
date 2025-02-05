# 如何在 JavaScript 中使用逻辑“或非”

要开始编写 JavaScript 代码，请访问终端/SSH 并输入 `node`。逻辑“或非”检查给定的参数是否都不为真。要返回两个值的逻辑或的反值，请使用逻辑非（`!`）运算符。以下是一个示例：

```js
const nor = (a, b) => !(a || b);
```

以下是一些输出结果：

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
