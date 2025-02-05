# 根据条件移除数组元素

要根据条件移除数组中的元素，请打开终端/SSH 并输入 `node`。

`takeWhile` 函数会从数组中移除元素，直到传入的函数返回 `false`，然后返回已移除的元素。

以下是使用 `takeWhile` 函数的步骤：

- 使用 `for...of` 循环遍历 `Array.prototype.entries()` 上的数组。
- 循环直到函数返回的值为假值。
- 使用 `Array.prototype.slice()` 返回已移除的元素。
- `fn` 回调函数接受一个参数，即元素的值。

使用以下代码实现 `takeWhile` 函数：

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

以下是使用 `takeWhile` 函数根据条件从数组中移除元素的示例：

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
