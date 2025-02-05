# 将可迭代对象转换为哈希

要将可迭代对象（对象或数组）转换为哈希（键控数据存储），请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.values()` 获取可迭代对象的值。
3. 使用 `Array.prototype.reduce()` 遍历这些值，并创建一个以引用值作为键的对象。
4. 使用可迭代对象和一个可选的键参数调用 `toHash` 函数，以指定引用值。

以下是 JavaScript 中 `toHash` 函数的一个示例实现：

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

你可以使用不同的可迭代对象和键调用 `toHash` 函数，以创建不同的哈希。例如：

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
