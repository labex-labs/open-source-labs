# 如何在 JavaScript 中从数组获取随机元素

要在 JavaScript 中从数组获取随机元素，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`Math.random()`方法生成一个介于 0（包括）和 1（不包括）之间的随机数。
3. 使用`Array.prototype.length`将随机数乘以数组的长度。
4. 使用`Math.floor()`将结果四舍五入为最接近的整数。
5. 使用舍入后的数字作为索引来从数组中访问随机元素。
6. 此方法也适用于字符串。

以下是演示此方法的代码片段：

```js
const getRandomElement = (arr) => arr[Math.floor(Math.random() * arr.length)];
```

你可以将`getRandomElement`函数与任何数组一起使用以获取随机元素。例如：

```js
getRandomElement([3, 7, 9, 11]); // 9
```
