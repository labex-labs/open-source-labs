# 检查一个数字是否为 2 的幂

要检查一个数字是否为 2 的幂，请按以下步骤操作：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用按位二进制与运算符（`&`）来确定数字（`n`）是否为 2 的幂。
3. 此外，检查`n`不为假值。
4. 以下代码在功能上检查`n`是否为 2 的幂：

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

以下是一些如何使用`isPowerOfTwo`函数的示例：

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
