# 编码及查找共同键的技巧

要练习编码，请打开终端/SSH并输入 `node`。

要查找两个对象之间的共同键，请执行以下步骤：

1. 使用 `Object.keys()` 获取第一个对象的键。
2. 使用 `Object.prototype.hasOwnProperty()` 检查第二个对象是否有第一个对象中的键。
3. 使用 `Array.prototype.filter()` 过滤掉不在两个对象中的键。

以下是代码示例：

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

你可以使用以下示例测试代码：

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
