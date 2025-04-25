# 检查数字是否为质数的函数

为了练习编码，打开终端/SSH 并输入`node`。此函数用于检查给定整数是否为质数。以下是检查一个数字是否为质数的步骤：

1. 检查从`2`到给定数字的平方根的所有数字。
2. 如果其中任何一个数字能整除给定数字，则返回`false`。
3. 如果没有任何一个数字能整除给定数字，则返回`true`，除非该数字小于`2`。

以下是用 JavaScript 实现此函数的代码：

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

你可以通过将一个数字作为参数调用该函数来测试它：

```js
isPrime(11); // true
```
