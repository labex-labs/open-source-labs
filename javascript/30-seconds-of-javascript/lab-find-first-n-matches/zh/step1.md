# 如何找到前 N 个匹配项

要找到满足特定条件的前 `n` 个元素，请使用 `findFirstN` 函数。具体方法如下：

1. 打开终端/SSH。
2. 输入 `node` 开始练习编码。
3. 使用 `findFirstN` 函数，传入要搜索的数组、一个匹配函数以及要查找的匹配项数量（如果未指定，默认值为 1）。
4. `matcher` 函数将对 `arr` 的每个元素执行，如果返回真值，则该元素将被添加到结果数组中。
5. 如果 `res` 数组的长度达到 `n`，函数将返回结果数组。
6. 如果未找到匹配项，则返回空数组。

以下是 `findFirstN` 函数的代码：

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

以下是一些使用示例：

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
