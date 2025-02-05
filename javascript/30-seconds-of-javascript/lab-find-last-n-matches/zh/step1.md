# 查找最后 N 个匹配项的说明

要查找满足特定条件的最后 `n` 个元素，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用下面提供的 `findLastN` 函数。
3. 提供一个数组 `arr` 和一个 `matcher` 函数，该函数为你要匹配的元素返回真值。
4. 你还可以选择提供要返回的匹配项数量 `n`（默认值为 1）。
5. 该函数将使用 `for` 循环从最后一个元素开始，对 `arr` 的每个元素执行 `matcher` 函数。
6. 如果某个元素符合 `matcher` 条件，它将使用 `Array.prototype.unshift()` 添加到结果数组中，该方法会将元素添加到数组开头。
7. 当结果数组的长度等于 `n` 时，函数将返回结果。
8. 如果没有匹配项，或者 `n` 大于匹配项的数量，则返回空数组。

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

以下是一些使用 `findLastN` 函数的示例：

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
