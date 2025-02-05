# 以下是将数组转换为标识对象的方法

如果你想练习编码，打开终端/SSH 并输入 `node`。要将一个值数组转换为一个键和值都相同的对象，请按以下步骤操作：

1. 使用 `Array.prototype.map()` 将每个值映射为一个键值对数组。
2. 使用 `Object.fromEntries()` 将键值对数组转换为一个对象。

以下是代码：

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

以下是一个示例：

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
