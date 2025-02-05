# 对函数使用逻辑或

要开始练习编码，请打开终端/SSH 并输入 `node`。

逻辑或 (`||`) 运算符可用于检查对于给定的一组参数，是否至少有一个函数返回 `true`。为此，使用提供的 `参数` 调用这两个函数，并对它们的结果应用逻辑或运算符。

以下是 `either` 函数的一个示例实现：

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

以下是 `either` 函数与两个函数 `isEven` 和 `isPositive` 的示例用法：

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

在这个示例中，`isPositiveOrEven` 对于 `4` 和 `3` 都返回 `true`，因为 `isEven` 对于 `4` 返回 `true`，而 `isPositive` 对于 `3` 返回 `true`。
