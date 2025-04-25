# 将函数转换为可变参数函数

要将一个接受数组的函数转换为可变参数函数，你可以按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。

2. 返回一个闭包，该闭包将所有输入收集到一个接受数组的函数中。

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. 使用 `collectInto` 函数将一个函数转换为可变参数函数。

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] （大约 2 秒后）
```

这样你就可以在函数中接受任意数量的参数，并将它们收集到一个数组中以便进一步处理。
