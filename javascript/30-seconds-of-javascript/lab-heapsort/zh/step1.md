# 堆排序算法

要进行编码练习，请打开终端/SSH并输入“node”。以下算法使用堆排序算法对数字数组进行排序。请按照以下步骤操作：

- 在函数中使用递归。
- 使用展开运算符（...）克隆原始数组`arr`。
- 使用闭包声明一个变量`l`和一个函数`heapify`。
- 使用`for`循环和`Math.floor()`并结合`heapify`从数组创建一个最大堆。
- 使用`for`循环反复缩小考虑的范围，使用`heapify`并在必要时交换值以对克隆数组进行排序。

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

例如：

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
