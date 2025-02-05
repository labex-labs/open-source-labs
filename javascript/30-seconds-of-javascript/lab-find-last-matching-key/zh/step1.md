# 查找符合条件的最后一个键的函数

要在对象中找到满足给定条件的最后一个键，请使用 `findLastKey` 函数。此函数接受一个对象和一个测试函数作为参数。如果找到匹配的键，函数将返回该键。否则，它将返回 `undefined`。以下是该函数查找最后一个键的步骤：

1. 使用 `Object.keys()` 获取对象的所有属性。
2. 使用 `Array.prototype.reverse()` 反转键的顺序。
3. 使用 `Array.prototype.find()` 对每个键值对测试提供的函数。回调函数接收三个参数 —— 值、键和对象。
4. 如果找到匹配的键，则返回它。

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

以下是使用 `findLastKey` 的示例：

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

要使用此函数，请打开终端/SSH 并输入 `node` 开始练习编码。
