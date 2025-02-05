# JavaScript 中的插入排序算法

要进行编码练习，请打开终端/SSH 并输入 `node`。此算法使用插入排序方法对数字数组进行排序。请按照以下步骤实现此算法：

1. 使用 `Array.prototype.reduce()` 遍历给定数组中的所有元素。
2. 如果累加器的 `length` 为 `0`，则将当前元素添加到其中。
3. 使用 `Array.prototype.some()` 遍历累加器中的结果，直到找到正确的位置。
4. 使用 `Array.prototype.splice()` 将当前元素插入到累加器中。

以下是在 JavaScript 中实现插入排序的代码：

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

你可以使用以下代码测试该算法：

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
