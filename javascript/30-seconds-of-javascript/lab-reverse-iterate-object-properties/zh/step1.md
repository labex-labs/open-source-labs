# 以下是如何反向遍历对象自身的属性

要以反向顺序遍历对象自身的属性并为每个属性运行一个回调函数，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.keys()` 获取对象的所有属性。
3. 使用 `Array.prototype.reverse()` 反转属性的顺序。
4. 使用 `Array.prototype.forEach()` 为每个键值对运行提供的函数。
5. 回调函数应该有三个参数：值、键和对象。

以下是代码：

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

你可以将此函数与任何对象和回调函数一起使用。例如，要以反向顺序记录 `{ foo: 'bar', a: 1 }` 的值，可以使用以下代码：

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
