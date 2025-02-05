# 使用埃拉托斯特尼筛法生成质数

要使用埃拉托斯特尼筛法生成指定数字以内的质数，请遵循以下步骤：

1. 打开终端/SSH并输入`node`以开始练习编码。
2. 创建一个包含从`2`到指定数字的数组。
3. 使用`Array.prototype.filter()`过滤掉能被从`2`到所提供数字的平方根之间的任何数字整除的值。
4. 返回包含质数的结果数组。

以下是生成指定数字以内质数的JavaScript代码：

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

你可以通过将所需数字作为参数传递来调用函数`generatePrimes()`。例如：

```js
generatePrimes(10); // [2, 3, 5, 7]
```
