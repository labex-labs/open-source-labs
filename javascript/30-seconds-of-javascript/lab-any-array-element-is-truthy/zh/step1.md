# 测试数组中是否有任何元素为真值

要开始练习编码，请打开终端/SSH 并输入 `node`。

要根据提供的函数检查集合中是否有任何元素返回 `true`，请使用 `Array.prototype.some()`。如果你想将 `Boolean` 函数用作默认值，可以省略第二个参数 `fn`。

以下是一个示例代码：

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

你可以使用以下示例进行测试：

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
