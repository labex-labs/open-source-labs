# 快速排序算法

为了练习编码，请打开终端/SSH 并输入`node`。此算法使用快速排序算法对数字数组进行排序。以下是具体步骤：

- 使用递归。
- 使用展开运算符（`...`）克隆原始数组`arr`。
- 如果数组的`length`小于`2`，则返回克隆后的数组。
- 使用`Math.floor()`计算枢轴元素的索引。
- 使用`Array.prototype.reduce()`和`Array.prototype.push()`将数组拆分为两个子数组。第一个子数组包含小于或等于`枢轴`的元素，第二个子数组包含大于它的元素。将结果解构为两个数组。
- 对创建的子数组递归调用`quickSort()`。

以下是实现此算法的示例：

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

要测试它，请运行以下命令：

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
