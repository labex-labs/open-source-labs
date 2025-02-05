# 将对象转换为键值对

要将对象转换为键值对数组，请使用 `toPairs` 函数。要开始编码，请打开终端/SSH 并输入 `node`。

`toPairs` 函数的工作方式如下：

- 首先，它检查给定的可迭代对象是否定义了 `Symbol.iterator`。
- 如果定义了 `Symbol.iterator`，它会使用 `Array.prototype.entries()` 获取对象的迭代器，然后使用 `Array.from()` 将结果转换为键值对数组的数组。
- 如果对象未定义 `Symbol.iterator`，则改为使用 `Object.entries()`。

以下是 `toPairs` 函数的代码：

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

你可以将 `toPairs` 函数与各种类型的对象一起使用，例如：

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0','s'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
