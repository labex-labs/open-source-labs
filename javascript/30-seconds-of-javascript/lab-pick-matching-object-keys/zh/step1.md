# 选取符合给定条件的对象键的函数

要选取符合给定条件的对象键，请使用 `pickBy()` 函数。此函数会创建一个新对象，该对象由给定函数返回真值的属性组成。

- 使用 `Object.keys()` 和 `Array.prototype.filter()` 来移除 `fn` 返回假值的键。
- 使用 `Array.prototype.reduce()` 将过滤后的键转换回具有相应键值对的对象。
- 回调函数会使用两个参数调用：(值，键)。

以下是 `pickBy()` 函数的代码：

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

你可以使用此函数来选取符合条件的键。例如：

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
