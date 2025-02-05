# 根据特定键将数组转换为对象

要根据特定键将数组转换为对象，并从每个值中排除该键，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `Array.prototype.reduce()` 从提供的数组创建一个对象。
- 使用对象解构提取给定 `key` 的值和相关的 `data`，然后将键值对添加到对象中。

以下是一个示例实现：

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

然后你可以像这样使用该函数：

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
