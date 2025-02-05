# 选择排序算法

要开始编码，请打开终端/SSH并输入 `node`。

以下函数使用选择排序算法对数字数组进行排序：

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

要使用此函数，将一个数字数组传递给 `selectionSort()`，如下所示：

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

该函数通过使用展开运算符 (`...`) 克隆原始数组来工作。然后，它使用 `for` 循环遍历数组。使用 `Array.prototype.slice()` 和 `Array.prototype.reduce()`，它在当前索引右侧的子数组中找到最小元素的索引。如有必要，它会进行交换。
