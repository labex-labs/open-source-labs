# 如何使用JavaScript在指定范围内生成随机整数

要使用JavaScript在指定范围内生成随机整数，请遵循以下步骤：

1. 打开终端/SSH并输入`node`以开始练习编码。
2. 使用`Math.random()`方法生成一个介于0（包括）和1（不包括）之间的随机数。
3. 将该随机数乘以范围的最大值与最小值之差，然后将最小值加到结果上，从而将随机数映射到所需范围。
4. 使用`Math.floor()`方法将结果向下舍入到最接近的整数。

以下是实现上述步骤的示例代码片段：

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

然后，你可以使用所需的最小值和最大值调用`randomIntegerInRange()`函数，以生成该范围内的随机整数。例如：

```js
randomIntegerInRange(0, 5); // 2
```
