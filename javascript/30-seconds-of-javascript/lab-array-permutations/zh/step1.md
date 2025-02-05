# 如何生成数组的所有排列

要开始练习编码，请打开终端/SSH 并输入 `node`。

以下是一个生成数组元素所有排列的算法（即使数组包含重复项）。按照以下步骤实现它：

1. 使用递归。
2. 对于给定数组中的每个元素，为其余元素创建所有部分排列。
3. 使用 `Array.prototype.map()` 将该元素与每个部分排列组合，然后使用 `Array.prototype.reduce()` 将所有排列组合成一个数组。
4. 基本情况是针对长度为 `2` 或 `1` 的数组。
5. 请注意，此函数的执行时间会随着数组元素数量呈指数级增长。超过 8 到 10 个元素可能会导致浏览器在尝试解决所有不同组合时挂起。

以下是代码：

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val
        ])
      ),
    []
  );
};
```

你可以通过使用数组参数调用 `permutations()` 函数来测试代码：

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
