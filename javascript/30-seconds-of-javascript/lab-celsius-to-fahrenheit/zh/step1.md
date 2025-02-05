# 摄氏温度转换为华氏温度

要通过编码将摄氏温度转换为华氏温度，请遵循以下步骤：

1. 打开终端/SSH。
2. 输入 `node`。
3. 使用转换公式：`F = 1.8 * C + 32`。
4. 使用以下代码实现该公式：

```js
const celsiusToFahrenheit = (degrees) => 1.8 * degrees + 32;
```

5. 通过输入摄氏温度值来测试该函数，如下所示：

```js
celsiusToFahrenheit(33); // 91.4
```

这将输出相应的华氏温度值。
