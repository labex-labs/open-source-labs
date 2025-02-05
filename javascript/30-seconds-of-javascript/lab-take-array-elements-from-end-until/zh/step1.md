# 从数组末尾移除元素，直到满足某个条件

要开始练习编码，请打开终端/SSH 并输入 `node`。

此函数从数组末尾移除元素，直到传入的函数返回 `true`，然后返回移除的元素。

它的工作原理如下：

- 首先，使用展开运算符 (`...`) 和 `Array.prototype.reverse()` 创建数组的反向副本。
- 接下来，使用 `for...of` 循环遍历 `Array.prototype.entries()` 返回的反向副本，直到函数返回的值为真值。
- 之后，使用 `Array.prototype.slice()` 返回移除的元素。
- 回调函数 `fn` 接受一个参数，即元素的值。

以下是代码：

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

以下是如何使用此函数的示例：

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
