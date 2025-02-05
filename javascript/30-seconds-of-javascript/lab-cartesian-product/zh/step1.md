# 笛卡尔积

要计算两个数组的笛卡尔积，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()`、`Array.prototype.map()` 和展开运算符（`...`）从这两个数组生成所有可能的元素对。
3. 使用以下代码：

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

示例：

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

这将生成这两个数组中所有可能的元素组合。
