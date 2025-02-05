# 如何在 JavaScript 中串联异步函数

要开始使用 JavaScript 进行编码练习，请打开终端/SSH 并输入 `node`。熟悉基础知识后，就可以开始使用异步函数了。

`pipeAsyncFunctions` 函数允许你使用异步函数进行从左到右的函数组合。它的工作原理如下：

- 该函数接受任意数量的异步函数作为参数。
- 展开运算符 (`...`) 用于将这些函数作为单独的参数传递给 `pipeAsyncFunctions` 函数。
- 结果函数可以接受任意数量的参数，但每个被组合的函数必须接受单个参数。
- 这些函数可以返回普通值、`Promise` 的组合，或者是 `async` 函数并通过 `await` 返回。
- `reduce()` 方法与 `Promise.prototype.then()` 一起用于执行函数组合。
- `reduce()` 方法遍历这些函数，依次执行每个函数，并将一个函数的结果传递给下一个函数。
- 返回最终的 `Promise`。

以下是一个如何使用 `pipeAsyncFunctions` 对数字求和的示例：

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4
);
(async () => {
  console.log(await sum(5)); // 15（一秒后）
})();
```

在这个示例中，`sum` 由四个函数组成，这些函数对输入数字添加不同的值。`sum` 的最终值是依次执行每个函数的结果，第二个函数有一秒的延迟。最后一个函数使用了 `async` 关键字以允许使用 `await`。

通过使用 `pipeAsyncFunctions`，你可以轻松地将任意数量的异步函数组合在一起，以创建更复杂的功能。
