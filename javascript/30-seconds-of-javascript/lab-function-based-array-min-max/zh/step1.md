# 如何使用给定函数找到数组的最小值和最大值

要进行编码练习，请打开终端或 SSH 并输入 `node`。

以下是一个函数，它根据给定的设置比较规则的函数返回数组的最小值和最大值：

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

要使用它，请执行以下步骤：

1. 使用要处理的数组和可选的 `comparator` 函数调用 `reduceWhich`。
2. `reduceWhich` 函数将结合使用 `Array.prototype.reduce()` 和 `comparator` 函数来返回数组中的合适元素。
3. 如果你省略第二个参数（`comparator`），将使用默认函数，该函数返回数组中的最小元素。

以下是一些如何使用 `reduceWhich` 的示例：

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

在上述示例中，第一次对 `reduceWhich` 的调用返回数组 `[1, 3, 2]` 的最小值，即 `1`。第二次调用根据反转比较顺序的 `comparator` 函数返回同一数组的最大值。第三次调用根据比较对象 `age` 属性的 `comparator` 函数返回数组中具有最小 `age` 属性的对象。
