# 使用函数为数组建立索引

要使用函数为数组建立索引，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()` 从数组创建一个对象。
3. 将提供的函数应用于数组的每个值以生成一个键，并将键值对添加到对象中。

以下是一个示例代码片段：

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

你可以按如下方式使用此函数：

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  (x) => x.id
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

此函数通过使用提供的函数将每个值映射到一个键，从而从数组创建一个对象。结果对象包含键值对，其中键由函数生成，值是原始数组元素。
