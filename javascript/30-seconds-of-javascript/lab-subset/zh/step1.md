# 检查一个可迭代对象的子集是否包含在另一个可迭代对象中

要进行编码练习，请打开终端/SSH 并输入 `node`。此函数检查第一个可迭代对象是否是第二个可迭代对象的子集，不包括重复值。

要实现这一点，你可以执行以下操作：

- 使用 `Set` 构造函数从每个可迭代对象创建一个新的 `Set` 对象。
- 使用 `Array.prototype.every()` 和 `Set.prototype.has()` 检查第一个可迭代对象中的每个值是否都包含在第二个可迭代对象中。

以下是一个示例实现：

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

你可以通过传入两个集合进行比较来使用 `subSet` 函数。例如：

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
