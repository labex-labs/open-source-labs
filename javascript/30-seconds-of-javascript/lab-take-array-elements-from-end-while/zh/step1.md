# 从数组末尾移除元素，直到满足某个条件

要开始练习编码，请打开终端/SSH 并输入 `node`。

下面是一个函数，它会从数组末尾移除元素，直到传入的函数返回 `false`。然后，它会返回被移除的元素。

要使用这个函数，使用展开运算符 (`...`) 和 `Array.prototype.reverse()` 创建数组的反向副本。然后，使用 `for...of` 循环遍历 `Array.prototype.entries()` 返回的反向副本，直到函数返回的值为假值。

回调函数 `fn` 接受一个参数，即元素的值。最后，使用 `Array.prototype.slice()` 返回被移除的元素。

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

下面是一个如何使用这个函数的示例：

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
