# 将对象转换为键值对数组

要将对象转换为键值对数组，请使用 `Object.keys()` 方法和 `Array.prototype.map()` 方法。这将遍历对象的键并生成一个包含键值对的数组。或者，你可以使用提供类似功能的 `Object.entries()` 方法。

以下是一个示例代码片段，展示了如何将对象转换为键值对数组：

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

你可以使用 `objectToEntries()` 函数将对象转换为键值对数组，如下所示：

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
