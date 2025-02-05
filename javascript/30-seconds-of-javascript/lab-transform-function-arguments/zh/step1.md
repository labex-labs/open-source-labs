# 转换函数参数

要转换函数参数，请使用 `overArgs` 函数，它会创建一个新函数，该函数使用转换后的参数调用提供的函数。

- 要转换参数，请结合使用 `Array.prototype.map()` 和展开运算符 (`...`)，并将转换后的参数传递给 `fn`。

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- 要测试 `overArgs` 函数，请创建一个示例函数和一个转换数组，然后使用参数调用新函数。

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
