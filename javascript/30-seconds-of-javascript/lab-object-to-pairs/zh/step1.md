# 将对象转换为键值对数组

要将一个对象转换为键值对数组，你可以遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.entries()` 方法从对象中获取一个键值对数组的数组。
3. 创建一个名为 `objectToPairs` 的函数，该函数接受一个对象作为参数并返回键值对数组。
4. 使用一个示例对象调用 `objectToPairs` 函数以测试输出。

以下是一个示例实现：

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

通过遵循这些步骤，你可以使用 JavaScript 轻松地将一个对象转换为键值对数组。
