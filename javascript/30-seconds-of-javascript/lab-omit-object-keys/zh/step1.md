# 从对象中移除键

要从对象中移除特定的键，可以使用 `omit` 函数，该函数接受一个对象和一个要移除的键的数组。

- `Object.keys()` 方法用于获取对象的所有键
- 然后使用 `Array.prototype.filter()` 方法从键列表中移除指定的键
- 最后，使用 `Array.prototype.reduce()` 创建一个包含剩余键值对的新对象

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

示例用法：

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
