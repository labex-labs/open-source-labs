# 参数合并工厂代码

要开始编码，请打开终端/SSH 并输入 `node`。此函数根据作为参数传递的验证器返回第一个计算结果为 `true` 的参数。

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

使用 `Array.prototype.find()` 从提供的参数验证函数 `valid` 中返回第一个返回 `true` 的参数。例如：

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

在这里，`coalesceFactory` 函数被定制以创建 `customCoalesce` 函数。`customCoalesce` 函数从提供的参数中过滤掉 `null`、`undefined`、`NaN` 和空字符串，并返回第一个未被过滤掉的参数。`customCoalesce(undefined, null, NaN, '', 'Waldo')` 的输出是 `'Waldo'`。
