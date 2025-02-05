# 判断值是否为对象

要判断传入的值是否为对象，请打开终端/SSH 并输入 `node`。具体步骤如下：

- `Object` 构造函数会为给定的值创建一个对象包装器。
- 如果值为 `null` 或 `undefined`，则创建并返回一个空对象。
- 如果值不是 `null` 或 `undefined`，则返回一个与给定值类型相对应的对象。

以下是一个检查值是否为对象的示例函数：

```js
const isObject = (obj) => obj === Object(obj);
```

以下是使用 `isObject` 函数的一些示例：

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
