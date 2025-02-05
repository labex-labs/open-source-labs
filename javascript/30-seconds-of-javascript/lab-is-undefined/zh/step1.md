# 检查是否为未定义值

要检查一个值是否为 `undefined`，请打开终端/SSH 并输入 `node`。

- 使用严格相等运算符检查 `val` 是否等于 `undefined`。

```js
const isUndefined = (val) => val === undefined;
```

```js
isUndefined(undefined); // true
```

这段代码将检查指定的值是否为 `undefined`。
