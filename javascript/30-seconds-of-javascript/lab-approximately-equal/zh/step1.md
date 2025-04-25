# 在 JavaScript 中检查数字是否近似相等

为了练习编码，打开终端/SSH 并输入 `node`。这段代码用于检查两个数字是否近似相等。具体做法如下：

- 使用 `Math.abs()` 方法将两个值的绝对差值与 `epsilon` 进行比较。
- 如果你没有提供第三个参数 `epsilon`，函数将使用默认值 `0.001`。

以下是代码：

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

要测试这个函数，你可以用两个数字作为参数调用它，如下所示：

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

这将返回 `true`，因为 `Math.PI / 2.0` 与 `1.5708` 近似相等，epsilon 为 `0.001`。
