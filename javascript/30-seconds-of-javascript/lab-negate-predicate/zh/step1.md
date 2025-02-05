# 如何在 JavaScript 中否定谓词函数

要在 JavaScript 中否定一个谓词函数，你可以使用 `!` 运算符。为此，你可以创建一个名为 `negate` 的高阶函数，它接受一个谓词函数，并将 `!` 运算符应用于该函数及其参数。以下是实现 `negate` 的示例：

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

然后，你可以使用 `negate` 来否定任何谓词函数。以下是如何使用 `negate` 从数组中过滤出偶数的示例：

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

在这个示例中，`isEven` 是一个检查数字是否为偶数的谓词函数。然后，我们使用 `negate` 创建一个名为 `isOdd` 的新谓词函数，通过否定 `isEven` 来检查数字是否为奇数。最后，我们将 `isOdd` 与 `filter` 方法一起使用，从数组中过滤出偶数。
