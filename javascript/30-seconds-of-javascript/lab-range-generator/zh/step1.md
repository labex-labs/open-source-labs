# 范围生成器

要使用给定的步长生成一系列值，请使用以下`rangeGenerator`函数。打开终端/SSH并输入`node`开始编码。

- 使用`while`循环和`yield`返回每个值，从`start`开始，到`end`结束。
- 如果你想使用默认步长`1`，则省略第三个参数。

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

以下是如何使用`rangeGenerator`函数的示例：

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// 输出 6, 7, 8, 9
```
