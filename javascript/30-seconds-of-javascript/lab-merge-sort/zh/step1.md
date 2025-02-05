# 归并排序算法

要使用归并排序算法进行编码练习，请遵循以下步骤：

1. 打开终端/SSH并输入 `node`。
2. 使用递归对数字数组进行排序。
3. 如果数组的 `length` 小于 `2`，则返回该数组。
4. 使用 `Math.floor()` 计算数组的中间点。
5. 使用 `Array.prototype.slice()` 将数组切成两半，并对创建的子数组递归调用 `mergeSort()`。
6. 最后，使用 `Array.from()` 和 `Array.prototype.shift()` 将两个已排序的子数组合并为一个。

以下是代码：

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

用这个例子试试：

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
