# 对函数进行柯里化

要对函数进行柯里化，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用递归。
3. 检查提供的参数数量（`args`）是否足够。
4. 如果足够，则调用传递的函数 `fn`。
5. 如果不足，则使用 `Function.prototype.bind()` 返回一个柯里化函数 `fn`，该函数等待其余的参数。
6. 如果你想对接受可变数量参数的函数（可变参数函数，例如 `Math.min()`）进行柯里化，则可以选择将参数数量传递给第二个参数 `arity`。
7. 使用以下代码：

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

以下是一些示例：

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
