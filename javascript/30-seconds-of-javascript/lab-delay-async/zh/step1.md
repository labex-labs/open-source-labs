# 如何在JavaScript中延迟异步函数的执行

要在JavaScript中延迟异步函数的执行，你可以使用下面的 `sleep` 函数，它返回一个 `Promise`，该 `Promise` 会在一定时间后 resolve。以下是一个如何使用 `sleep` 延迟 `async` 函数一部分执行的示例：

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("我要睡1秒钟。");
  await sleep(1000);
  console.log("1秒钟后我醒来了。");
}
```

要使用此函数，只需调用 `sleepyWork()`，控制台就会按顺序输出消息，两条消息之间间隔1秒钟。
