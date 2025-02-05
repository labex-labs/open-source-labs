# 用于映射对象值的函数

要使用提供的函数来映射对象的值，以生成一个具有相同键的新对象，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.keys()` 遍历对象的键。
3. 使用 `Array.prototype.reduce()` 使用提供的函数 `fn` 创建一个具有相同键和映射值的新对象。
4. 以下代码演示了 `mapValues` 函数的实现。

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

以下是 `mapValues` 函数的一个示例用法：

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
