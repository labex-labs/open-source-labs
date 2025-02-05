# 将数组映射到对象

要使用函数将数组的值映射到对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始编码练习。
2. 使用 `Array.prototype.reduce()` 将 `fn` 应用于 `arr` 中的每个元素，并将结果组合成一个对象。
3. 将 `el` 用作每个属性的键，并将 `fn` 的结果用作值。

以下是一个示例代码片段：

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

你可以按如下示例使用 `mapObject` 函数：

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
