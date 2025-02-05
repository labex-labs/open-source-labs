# 在 JavaScript 中将值转换为数组

要将一个值转换为数组，请使用下面提供的 `castArray` 函数。

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

要使用此函数，请将要转换的值作为参数传递。该函数将使用 `Array.isArray()` 检查该值是否已经是一个数组。如果是数组，函数将按原样返回它。如果不是数组，函数将返回封装在数组中的值。

以下是如何使用 `castArray` 的示例：

```js
castArray("foo"); // 返回: ['foo']
castArray([1]); // 返回: [1]
```

要开始练习 JavaScript 编码，请打开终端或 SSH 并输入 `node`。
