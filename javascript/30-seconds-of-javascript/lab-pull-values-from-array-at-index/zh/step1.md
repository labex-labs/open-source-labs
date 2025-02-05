# 如何从数组的指定索引处提取值

要从数组的特定索引处提取特定值，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.filter()` 和 `Array.prototype.includes()` 过滤掉不需要的值，并将它们存储在一个名为 `removed` 的新数组中。
3. 将 `Array.prototype.length` 设置为 `0`，通过重置其长度来改变原始数组。
4. 使用 `Array.prototype.push()` 仅用提取的值重新填充原始数组。
5. 使用 `Array.prototype.push()` 跟踪被移除的值。
6. 函数 `pullAtIndex` 接受两个参数：原始数组和要提取的索引数组。
7. 该函数返回一个被移除值的数组。

示例用法：

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
