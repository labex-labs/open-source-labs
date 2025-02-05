# 循环生成器说明

要开始练习编码，请打开终端/SSH 并输入 `node`。然后，创建一个无限循环遍历给定数组的生成器。以下是步骤：

1. 使用一个不会终止的 `while` 循环，每次调用 `Generator.prototype.next()` 时都会 `yield` 一个值。
2. 将取模运算符 (`%`) 与 `Array.prototype.length` 一起使用，以获取下一个值的索引，并在每次 `yield` 语句后增加计数器。

以下是 `cycleGenerator` 函数的示例：

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

然后你可以按如下方式使用该函数：

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

按照这些说明，你可以创建一个无限循环遍历任何数组的循环生成器。
