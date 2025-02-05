# 如何从数组中提取匹配的值

要使用 JavaScript 从数组中提取特定的值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.filter()` 和 `Array.prototype.includes()` 过滤掉不需要的值并创建一个新数组。
3. 设置 `Array.prototype.length` 以通过将原始数组的长度重置为 `0` 来变异原始数组。
4. 使用 `Array.prototype.push()` 仅用提取的值重新填充原始数组。
5. 使用 `Array.prototype.push()` 在一个新数组中跟踪移除的值。

以下是一个实现这些步骤的示例函数：

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

你可以使用此函数从数组中移除特定的值并返回移除的元素，如下所示：

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
