# 生成值直到满足给定条件

要开始练习编码，请打开终端/SSH 并输入 `node`。完成此操作后，你可以创建一个生成器，该生成器会生成新值，直到满足给定条件为止。

要创建此生成器，请按照以下步骤操作：

- 使用 `seed` 值初始化当前的 `val`。
- 使用 `while` 循环，在使用当前 `val` 调用 `condition` 函数返回 `false` 时持续迭代。
- 使用 `yield` 关键字返回当前的 `val`，并可选择接收一个新的种子值 `nextSeed`。
- 使用 `next` 函数根据当前的 `val` 和 `nextSeed` 计算下一个值。

以下是一个示例代码片段：

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

你可以通过使用适当的参数调用生成器来使用它。例如：

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

这将生成一个从 `1` 到 `5` 的值数组，因为当 `val` 等于 `6` 时满足条件 `v > 5`。
