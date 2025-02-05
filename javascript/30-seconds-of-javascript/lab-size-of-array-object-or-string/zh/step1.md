# 获取数组、对象或字符串大小的函数

要使用此函数，请打开终端/SSH并输入 `node`。此函数用于获取数组、对象或字符串的大小。

使用方法如下：

- 确定 `val` 的类型（`array`、`object` 或 `string`）。
- 对于数组，使用 `Array.prototype.length` 属性。
- 如果可用，使用 `length` 或 `size` 值，对于对象则使用键的数量。
- 对于字符串，使用从 `val` 创建的[`Blob` 对象](https://developer.mozilla.org/en-US/docs/Web/API/Blob)的 `size`。

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

示例：

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
