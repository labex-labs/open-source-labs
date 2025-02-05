# 反转函数组合

要开始练习编码，请打开终端/SSH 并输入 `node`。

以下是如何进行从左到右的函数组合：

- 使用 `Array.prototype.reduce()` 方法进行从左到右的函数组合。
- 第一个（最左边的）函数可以接受一个或多个参数，而其余函数必须是一元函数。

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

例如：

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
