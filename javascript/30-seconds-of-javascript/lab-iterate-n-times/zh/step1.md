# 代码实践：迭代 N 次

为了练习编码，打开终端/SSH 并输入 `node`。完成此操作后，使用以下函数对回调函数迭代 `n` 次：

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

要使用此函数，请调用 `times()` 并传入以下参数：

- `n`：你想要对回调函数进行迭代的次数
- `fn`：你想要迭代的回调函数
- `context`（可选）：你想要用于回调函数的上下文（如果未指定，在非严格模式下它将使用 `undefined` 对象或全局对象）

以下是使用 `times()` 函数的示例：

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

这将对回调函数 `i => (output += i)` 迭代 5 次，并将输出存储在 `output` 变量中。然后，输出将被记录到控制台，显示为 `01234`。
