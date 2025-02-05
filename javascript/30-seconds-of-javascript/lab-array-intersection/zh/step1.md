# 查找数组交集

要找出两个数组之间的共同元素并去除重复项，请使用以下代码：

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

要使用此代码，请打开终端/SSH 并输入 `node`。然后使用两个数组作为参数调用 `intersection` 函数，如下所示：

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

这将返回一个包含两个数组中都存在的元素的数组，且去除了重复项。
