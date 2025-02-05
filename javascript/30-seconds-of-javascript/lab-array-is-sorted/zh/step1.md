# 代码练习：检查数组是否已排序

为了练习编码，请打开终端/SSH 并输入 `node`。

以下是一个用于检查数字数组是否已排序的函数：

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

要使用它，请将一个数字数组传递给 `isSorted()`。如果数组按升序排序，该函数将返回 `1`；如果按降序排序，返回 `-1`；如果未排序，则返回 `0`。

以下是一些示例：

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
