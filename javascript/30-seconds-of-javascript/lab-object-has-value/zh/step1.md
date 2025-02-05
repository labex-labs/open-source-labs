# 检查对象是否包含特定值的函数

要检查一个对象是否包含特定值，请使用以下函数：

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

要使用此函数，请将你要搜索的对象和目标值作为参数传入。如果对象包含该值，函数将返回 `true`；如果不包含，则返回 `false`。

以下是一个示例：

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

要开始编码，请打开终端/SSH 并输入 `node`。
