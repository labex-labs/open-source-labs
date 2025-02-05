# 如何检查两个数组是否有共同元素

要检查两个数组是否有共同元素，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 从 `b` 创建一个 `Set` 以获取 `b` 中的唯一值。
3. 在 `a` 上使用 `Array.prototype.some()`，通过 `Set.prototype.has()` 检查其任何值是否包含在 `b` 中。
4. 使用下面提供的 `intersects` 函数来测试数组。

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

使用 `intersects` 函数检查两个数组是否相交：

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

通过遵循这些步骤并使用提供的代码，你可以轻松检查两个数组是否有共同元素。
