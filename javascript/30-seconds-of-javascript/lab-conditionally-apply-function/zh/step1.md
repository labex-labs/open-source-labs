# 使用 `when` 函数应用条件

要在满足特定条件时应用一个函数，请使用 `when` 函数。首先，打开终端/SSH 并输入 `node`。

`when` 函数返回一个新函数，该新函数接受一个参数，如果该参数为真值，则运行一个回调函数；如果该参数为假值，则返回该参数。该函数接受一个单一值 `x`，并根据 `pred` 参数返回适当的值。

以下是 `when` 函数的一个示例实现：

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

你可以使用 `when` 函数创建一个新函数，该函数将偶数翻倍：

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
