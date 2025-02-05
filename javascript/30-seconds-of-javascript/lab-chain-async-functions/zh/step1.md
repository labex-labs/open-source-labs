# 链式调用异步函数

要链式调用异步函数，请打开终端/SSH并输入 `node`。然后，遍历包含异步事件的函数数组，并在每个异步事件完成时调用 `next` 函数。

以下是一个演示如何链式调用异步函数的代码片段：

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 秒");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 秒");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 秒");
  }
]);
```
