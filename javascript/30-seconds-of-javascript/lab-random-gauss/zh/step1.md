# 使用 Box-Muller 变换生成高斯随机数

要使用 Box-Muller 变换生成高斯（正态分布）随机数，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用提供的代码片段，该代码片段利用 Box-Muller 变换生成具有高斯分布的随机数。
3. 代码片段中提供的 `randomGauss()` 函数生成具有高斯分布的随机数。
4. `randomGauss()` 函数的输出是一个介于 0 和 1 之间的数字。
5. 该输出可用于各种应用，例如统计模拟、数据分析和机器学习。

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

示例用法：

```js
randomGauss(); // 0.5
```
