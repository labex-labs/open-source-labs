# 数组差异

要找出两个数组之间的差异，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始编码。

2. 从数组 `b` 创建一个 `Set`，以从 `b` 中提取唯一值。

3. 在数组 `a` 上使用 `Array.prototype.filter()`，通过 `Set.prototype.has()` 仅保留不在数组 `b` 中的值。

以下是代码：

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

示例用法：

```js
difference([1, 2, 3, 3], [1, 2, 4]); // 输出：[3, 3]
```
