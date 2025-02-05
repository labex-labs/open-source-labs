# 查找与测试匹配的首个键的函数

要在对象中查找与给定测试函数匹配的首个键，请使用 `findKey()` 函数。首先，使用 `Object.keys()` 获取对象的所有属性。然后，使用 `Array.prototype.find()` 将测试函数应用于每个键值对。测试函数应接受三个参数：值、键和对象。如果找到满足测试函数的首个键，则该函数返回该键；如果未找到，则返回 `undefined`。

以下是 `findKey()` 的一个示例实现：

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

要使用 `findKey()`，请将对象和测试函数作为参数传入：

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

在此示例中，`findKey()` 返回对象中 `active` 属性值为 `true` 的首个键，即 `'barney'`。
