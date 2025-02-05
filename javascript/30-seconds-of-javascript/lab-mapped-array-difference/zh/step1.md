# 通过映射返回两个数组差异的函数

要开始编码，请打开你的终端/SSH 并输入 `node`。

此函数接受两个数组，并对两个数组中的每个元素应用提供的函数，以返回它们的差异。

具体做法如下：

- 通过对第二个数组（`b`）中的每个元素应用函数（`fn`）来创建一个 `Set`。
- 使用 `Array.prototype.map()` 对第一个数组（`a`）中的每个元素应用函数（`fn`）。
- 在第一个数组（`a`）上结合使用 `Array.prototype.filter()` 和函数（`fn`），使用 `Set.prototype.has()` 仅保留第二个数组（`b`）中不包含的值。

以下是该函数的代码：

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

以下是一些使用该函数的示例：

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
