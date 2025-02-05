# 连续值数组

要在 JavaScript 中创建一个连续值的数组，可以使用 `Array.prototype.reduce()` 方法。该方法将一个函数应用于累加器和数组中的每个元素，从左到右，并返回一个连续缩减值的数组。

以下是如何使用 `reduceSuccessive` 函数将给定函数应用于给定数组，并存储每个新结果：

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

然后，可以使用一个数组、一个函数和累加器的初始值来调用 `reduceSuccessive` 函数：

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

要开始使用这个函数进行编码练习，请打开终端/SSH 并输入 `node`。
