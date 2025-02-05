# 测量函数执行时间

要测量函数执行所花费的时间，请使用 `console.time()` 和 `console.timeEnd()` 来确定开始时间和结束时间之间的差异。

以下是一个名为 `timeTaken` 的示例函数，用于测量回调函数执行所花费的时间：

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

要使用此函数，只需将你的回调函数作为参数传入即可。例如：

```js
timeTaken(() => Math.pow(2, 10)); // 返回 1024，并输出：timeTaken: 0.02099609375ms
```

在上述示例中，`timeTaken` 函数用于测量执行 `Math.pow(2, 10)` 函数调用所花费的时间，该调用返回 1024。控制台输出将显示以毫秒（ms）为单位的执行时间。
