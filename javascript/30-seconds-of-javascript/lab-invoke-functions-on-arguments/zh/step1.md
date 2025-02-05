# 对参数调用函数

要使用 Node.js 执行代码，请打开终端/SSH 并输入 `node`。

要创建一个函数，该函数使用接收到的参数调用每个提供的函数并返回结果：

- 使用 `Array.prototype.map()` 和 `Function.prototype.apply()` 将每个函数应用于给定的参数。

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

示例：

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
