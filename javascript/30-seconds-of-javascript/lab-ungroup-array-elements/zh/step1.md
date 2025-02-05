# 如何在 JavaScript 中解组数组元素

要解组由 `zip` 函数生成的数组中的元素，可以使用 JavaScript 中的 `unzip` 函数创建一个二维数组。具体步骤如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Math.max()`、`Function.prototype.apply()` 获取数组中最长的子数组，并使用 `Array.prototype.map()` 使每个元素成为一个数组。
3. 使用 `Array.prototype.reduce()` 和 `Array.prototype.forEach()` 将分组的值映射到各个数组。

以下是 `unzip` 函数的代码：

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

你可以通过以下示例使用 `unzip` 函数：

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

按照这些步骤，你可以轻松地在 JavaScript 中解组数组元素。
