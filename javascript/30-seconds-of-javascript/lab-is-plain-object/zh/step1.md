# 检查一个值是否为普通对象

要检查一个值是否为普通对象，请执行以下步骤：

- 检查该值是否为真值。
- 使用 `typeof` 检查它是否为对象。
- 使用 `Object.prototype.constructor` 确保构造函数等于 `Object`。

使用以下代码实现此检查：

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

你可以使用以下示例测试此函数：

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
