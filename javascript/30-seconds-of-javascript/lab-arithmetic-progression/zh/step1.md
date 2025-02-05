# 算术级数代码示例

要进行编码练习，请打开终端/SSH并输入 `node`。

以下是一个创建算术级数数字数组的示例代码。该数组从给定的正整数开始，一直到指定的限制：

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

要使用此代码，只需使用两个参数调用函数 `arithmeticProgression`：起始正整数和限制。例如：

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
