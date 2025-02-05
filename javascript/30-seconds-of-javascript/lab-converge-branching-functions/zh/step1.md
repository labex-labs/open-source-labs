# 收敛函数

要进行编码练习，请打开终端/SSH 并输入 `node`。

这个函数 `converge` 接受一个收敛函数和一系列分支函数作为输入。它返回一个新函数，该新函数将每个分支函数应用于输入参数。然后，分支函数的结果作为参数传递给收敛函数。

`Array.prototype.map()` 和 `Function.prototype.apply()` 方法用于将每个函数应用于输入参数。然后，展开运算符 (`...`) 用于使用所有其他函数的结果调用 `converger`。

以下是 `converge` 函数的代码：

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

下面展示了如何使用这个函数的一个示例。通过使用一个计算数组平均值的匿名函数调用 `converge` 来创建 `average` 函数。分支函数是两个分别计算数组总和及其长度的匿名函数。

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

这段代码计算数组 `[1, 2, 3, 4, 5, 6, 7]` 的平均值并返回 `4`。
