# 如何使用 NodeJS 将华氏温度转换为摄氏温度

要开始练习编码，请打开终端/SSH 并输入`node`。然后，按照以下步骤将华氏温度转换为摄氏温度：

1. 使用转换公式`C = (F - 32) * 5 / 9`。
2. 在 NodeJS 中创建一个函数来应用该公式：

```js
const fahrenheitToCelsius = (degrees) => ((degrees - 32) * 5) / 9;
```

3. 通过输入一个华氏度数作为参数来测试该函数：

```js
fahrenheitToCelsius(32); // 0
```

按照这些步骤，你可以使用 NodeJS 轻松地将温度从华氏度转换为摄氏度。
