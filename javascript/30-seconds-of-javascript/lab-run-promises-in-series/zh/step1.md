# 依次运行 Promise

要依次执行一系列 Promise，请使用 `Array.prototype.reduce()` 创建一个 Promise 链。每个 Promise 在解决后返回下一个 Promise。

首先，打开终端/SSH 并输入 `node` 开始练习编码。

以下是代码示例：

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

然后，你可以使用 `runPromisesInSeries` 函数按顺序执行 Promise，如下例所示：

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// 这段代码按顺序运行每个 Promise，总共需要 3 秒才能完成。
```
