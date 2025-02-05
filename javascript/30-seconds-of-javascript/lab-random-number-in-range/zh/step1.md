# 如何使用 JavaScript 在给定范围内生成随机数

要使用 JavaScript 在指定范围内生成随机数，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Math.random()` 方法生成一个随机值。
3. 通过乘法将生成的值映射到所需范围。
4. 使用以下代码创建一个在给定范围内生成随机数的函数：

```js
const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;
```

5. 要使用该函数，请传入所需范围的最小值和最大值作为参数。例如：

```js
randomNumberInRange(2, 10); // 6.0211363285087005
```

通过遵循这些步骤，你可以轻松地使用 JavaScript 在给定范围内生成随机数。
