# 根据键值对创建对象

要根据键值对创建对象，请使用 `objectFromPairs` 函数。

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 该函数使用 `Array.prototype.reduce()` 来创建并组合键值对。
- 对于更简单的实现，你也可以使用[`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries)。

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

示例用法：

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
