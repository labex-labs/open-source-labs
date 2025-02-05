# 计算最小公倍数

要计算两个或多个数字的最小公倍数，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用最大公约数（GCD）公式以及 `lcm(x, y) = x * y / gcd(x, y)` 这一事实来确定最小公倍数。
3. GCD 公式使用递归。
4. 在 JavaScript 中实现以下代码：

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

示例用法：

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
