# 防抖Promise

要创建一个返回Promise的防抖函数，该函数会延迟调用提供的函数，直到自上次调用以来至少经过了 `ms` 毫秒，请按以下步骤操作：

1. 每次调用防抖函数时，使用 `clearTimeout()` 清除当前挂起的超时，然后使用 `setTimeout()` 创建一个新的超时，该超时会延迟调用函数，直到至少经过了 `ms` 毫秒。
2. 使用 `Function.prototype.apply()` 将 `this` 上下文应用于函数并提供必要的参数。
3. 创建一个新的 `Promise`，并将其 `resolve` 和 `reject` 回调添加到挂起的Promise堆栈中。
4. 当调用 `setTimeout()` 时，复制当前堆栈（因为在提供的函数调用与其解析之间它可能会改变），清除它并调用提供的函数。
5. 当提供的函数解析/拒绝时，使用返回的数据解析/拒绝堆栈中的所有Promise（在调用函数时复制）。
6. 省略第二个参数 `ms`，将超时设置为默认的 `0` 毫秒。

以下是 `debouncePromise()` 函数的代码：

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

以下是如何使用 `debouncePromise()` 的示例：

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// 两次都会输出 ['resolved', 'bar']
```
