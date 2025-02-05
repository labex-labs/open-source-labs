# 根据回调函数移除对象键

要根据回调函数移除对象键，请使用 `omitBy` 函数。

- `omitBy` 创建一个对象，该对象由对给定函数返回假值的属性组成。
- `Object.keys()` 和 `Array.prototype.filter()` 用于移除 `fn` 返回真值的键。
- `Array.prototype.reduce()` 将过滤后的键转换回具有相应键值对的对象。
- 回调函数接受两个参数：`value` 和 `key`。
- 以下示例展示了如何使用 `omitBy` 从对象中移除数字键。

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
