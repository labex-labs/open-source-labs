# 如何在JavaScript中从数组获取加权样本

要根据提供的权重从数组中随机获取一个元素，请遵循以下步骤：

1. 打开终端/SSH并输入`node`以开始练习编码。
2. 使用`Array.prototype.reduce()`为`weights`中的每个值创建一个部分和的数组。
3. 使用`Math.random()`生成一个随机数，并使用`Array.prototype.findIndex()`根据先前生成的数组找到正确的索引。
4. 最后，返回`arr`中具有生成索引的元素。

以下是实现此目的的代码：

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

你可以通过将数组及其相应的权重作为参数传递来测试此函数：

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
