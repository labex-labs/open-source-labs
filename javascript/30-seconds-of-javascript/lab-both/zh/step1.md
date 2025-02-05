# 对函数使用逻辑与运算符

要开始练习编码，请打开终端/SSH 并输入 `node`。

要检查两个函数对于给定的一组参数是否返回 `true`，请使用逻辑与 (`&&`) 运算符。

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

上述代码创建了一个新函数 `both`，它接受两个函数 `f` 和 `g` 作为输入，并返回另一个函数，该函数使用提供的参数调用 `f` 和 `g`，并且仅当两个函数都返回 `true` 时才返回 `true`。

例如，要检查一个数字是否既是正数又是偶数，我们可以将 `isEven` 和 `isPositive` 函数与 `both` 一起使用，如下所示：

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

在这里，`isPositiveEven` 是一个新函数，它通过将 `both` 函数与 `isEven` 和 `isPositive` 作为输入来检查给定的数字是否既是正数又是偶数。
