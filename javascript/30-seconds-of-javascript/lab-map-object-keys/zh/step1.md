# 用于映射对象键的函数

要使用提供的函数映射对象的键并生成新对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Object.keys()` 遍历对象的键。
3. 使用 `Array.prototype.reduce()` 创建一个新对象，该对象具有相同的值，并且使用提供的函数（`fn`）映射键。

以下是 `mapKeys` 函数的示例实现：

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

你可以使用如下示例输入来测试该函数：

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
