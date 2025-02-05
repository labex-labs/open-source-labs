# 以下是在 JavaScript 中将数字四舍五入到给定精度的方法：

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- 使用 `Math.round()` 和模板字面量将数字四舍五入到指定的位数。
- 如果你想四舍五入到整数，省略第二个参数 `decimals`。
- 要开始练习编码，请打开终端/SSH 并输入 `node`。
- 例如，`round(1.005, 2)` 将返回 `1.01`。
