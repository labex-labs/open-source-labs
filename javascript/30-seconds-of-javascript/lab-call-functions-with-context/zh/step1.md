# 如何在 JavaScript 中使用上下文调用函数

要在 Node.js 中执行代码，请打开终端/SSH 并输入 `node`。如果你想在 JavaScript 中使用特定的上下文和一组参数来调用函数，可以使用闭包。以下是实现方法：

1. 定义一个名为 `call` 的函数，它接受一个 `key` 和一组 `args` 作为参数，并返回一个新函数，该新函数接受一个 `context` 参数。

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. 使用 `call` 函数对一个数字数组调用 `map` 函数。在这个例子中，`map` 函数将数组中的每个数字翻倍。

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. 你还可以将 `call` 函数绑定到特定的键，比如 `map`，并使用它对一个数字数组调用 `map` 函数。

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

通过使用 `call` 函数，你可以轻松地使用特定的上下文和参数集来调用任何函数。
