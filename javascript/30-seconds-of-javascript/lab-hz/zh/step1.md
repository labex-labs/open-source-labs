# 函数频率计算

要测量每秒函数执行的频率（赫兹），可使用 `hz` 函数。你可以按以下步骤进行：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `performance.now()` 获取迭代循环前后的毫秒数差异，以计算执行函数 `iterations` 次所花费的时间。
3. 将毫秒数转换为秒数，并除以所花费的时间，以返回每秒的周期数。
4. 如果你想使用默认的 100 次迭代，可省略第二个参数 `iterations`。

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

以下是使用 `hz` 函数比较两个计算 10000 个数组之和的函数性能的示例：

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

在这个示例中，`sumReduce` 比 `sumForLoop` 更快，因为它的函数执行频率更低。
