# 转换可变参数函数

要转换可变参数函数，请按以下步骤操作：

1. 打开终端/SSH并输入`node`以开始编码。
2. 创建一个接受可变参数函数的函数。
3. 使用闭包和展开运算符（`...`）将参数数组映射到函数的输入。
4. 返回一个新函数，该函数接受参数数组并用这些参数调用原始可变参数函数。

以下是如何使用此技术转换`Math.max`函数的示例：

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
