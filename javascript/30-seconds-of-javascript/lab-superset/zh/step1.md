# 检查一个集合是否是另一个集合的超集的函数

要检查一个集合是否是另一个集合的超集，请使用 `superSet()` 函数。首先，打开终端/SSH 并输入 `node` 以开始练习编码。然后，按照以下步骤操作：

- 使用 `Set` 构造函数从每个可迭代对象创建一个新的 `Set` 对象。
- 使用 `Array.prototype.every()` 和 `Set.prototype.has()` 检查第二个可迭代对象中的每个值是否都包含在第一个可迭代对象中。
- 如果第一个可迭代对象是第二个可迭代对象的超集（排除重复值），则该函数返回 `true`。否则，返回 `false`。

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

使用两个集合作为参数调用 `superSet()`，以检查一个集合是否是另一个集合的超集。

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
