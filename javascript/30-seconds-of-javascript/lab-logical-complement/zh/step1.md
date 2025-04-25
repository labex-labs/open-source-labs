# 逻辑补码

要开始练习编码，请打开终端/SSH 并输入 `node`。

要获取函数 `fn` 的逻辑补码，请使用 `complement` 函数。此函数返回另一个函数，该函数对使用提供的任何参数调用 `fn` 的结果应用逻辑非 (`!`) 运算符。

以下是一个示例代码片段：

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

要使用此函数，请定义一个谓词函数，例如 `isEven`，如果给定数字是偶数，则返回 `true`。然后，你可以使用 `complement` 函数获取此函数的逻辑补码，如下所示：

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
