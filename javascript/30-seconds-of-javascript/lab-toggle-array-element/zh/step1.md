# 如何切换数组中的元素

要在数组中切换元素，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.includes()` 检查给定元素是否在数组中。
3. 如果元素在数组中，使用 `Array.prototype.filter()` 将其移除。
4. 如果元素不在数组中，使用展开运算符 (`...`) 将其添加。
5. 使用 `toggleElement` 函数（它接受一个数组和一个值）来切换数组中的元素。

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

按照这些步骤操作，你可以使用 JavaScript 轻松地在数组中切换元素。
