# 最多接受两个参数的函数

要开始编码，请打开终端/SSH 并输入 `node`。

创建了 `binary` 函数，它能够接受最多两个参数，同时忽略任何其他参数。

使用给定的前两个参数调用提供的 `fn` 函数。

以下是代码：

```js
const binary = (fn) => (a, b) => fn(a, b);
```

以下是一个示例用法：

```js
["2", "1", "0"].map(binary(Math.max)); // [2, 1, 2]
```
