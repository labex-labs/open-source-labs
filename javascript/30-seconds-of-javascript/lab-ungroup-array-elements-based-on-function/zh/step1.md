# 如何根据函数对数组元素进行解组

如果你需要对 `zip` 生成的数组中的元素进行解组并应用一个函数，可以使用 `unzipWith`。以下是实现方法：

1. 使用 `Math.max()` 和展开运算符 (`...`) 获取数组中最长的子数组，并使用 `Array.prototype.map()` 使每个元素成为一个数组。
2. 使用 `Array.prototype.reduce()` 和 `Array.prototype.forEach()` 将分组的值映射到各个数组。
3. 使用 `Array.prototype.map()` 和展开运算符 (`...`) 对每个单独的元素组应用 `fn`。

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

要使用 `unzipWith`，打开终端/SSH 并输入 `node`。然后，你可以运行以下示例：

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

这将通过对 `zip` 生成的输入数组中的元素进行解组并应用提供的函数来创建一个元素数组。
