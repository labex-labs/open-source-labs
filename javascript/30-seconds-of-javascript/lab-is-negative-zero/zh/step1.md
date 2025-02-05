# 检查是否为负零

要检查一个数字是否为负零，请打开终端/SSH 并输入 `node`。然后，使用以下代码：

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

这将检查传入的值是否等于 `0`，以及 `1` 除以该值是否等于 `-Infinity`。例如：

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
