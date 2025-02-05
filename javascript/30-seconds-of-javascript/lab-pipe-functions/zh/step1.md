# 使用管道进行函数组合

要开始使用管道进行编码练习，请打开终端/SSH 并输入 `node`。

`pipeFunctions` 函数使用 `Array.prototype.reduce()` 和展开运算符 (`...`) 来执行从左到右的函数组合。第一个（最左边的）函数可以接受一个或多个参数，而其余函数必须是一元函数。

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

以下是一个如何使用 `pipeFunctions` 创建新函数 `multiplyAndAdd5` 的示例，该函数将两个数字相乘，然后将 5 加到结果上：

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

在这个示例中，`multiplyAndAdd5` 是一个新函数，它接受两个参数 `5` 和 `2`，首先对它们应用 `multiply`，结果为 `10`，然后对结果应用 `add5`，结果为 `15`。
