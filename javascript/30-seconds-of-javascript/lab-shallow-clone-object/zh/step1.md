# 如何创建对象的浅克隆

要创建对象的浅克隆，请使用 `Object.assign()` 和一个空对象 (`{}`)。请按照以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用以下代码创建原始对象的浅克隆：

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3. 要克隆对象，请按如下方式使用 `shallowClone()` 函数：

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a 不等于 b
```

在此示例中，`a` 和 `b` 是两个不同的对象，但它们具有相同的值。
