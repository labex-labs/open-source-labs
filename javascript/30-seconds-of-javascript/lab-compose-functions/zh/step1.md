# 如何在 JavaScript 中进行函数组合

要开始使用 JavaScript 中的函数组合进行编码练习，请打开终端/SSH 并输入 `node`。

以下是在 JavaScript 中如何执行从右到左的函数组合的示例：

1. 使用 `Array.prototype.reduce()` 来执行从右到左的函数组合。
2. 最后一个（最右边的）函数可以接受一个或多个参数；其余函数必须是一元函数。
3. 定义 `compose` 函数，它将接受任意数量的函数作为参数，并返回一个将它们组合起来的新函数。
4. 按照所需顺序使用所需函数调用 `compose` 函数。
5. 使用任何必要的参数调用新的组合函数。

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

例如，假设我们有两个函数：

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

我们可以使用 `compose` 来组合这些函数：

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

现在我们可以使用所需的参数调用 `multiplyAndAdd5`：

```js
multiplyAndAdd5(5, 2); // 15
```
