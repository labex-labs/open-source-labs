# 当条件为真时生成值的生成器

要开始编码，请打开终端/SSH并输入 `node`。这将创建一个生成器，只要满足给定条件，它就会持续生成新值。

生成器使用一个 `seed` 值进行初始化，该值用于初始化当前的 `val`。然后使用一个 `while` 循环进行迭代，只要使用当前 `val` 调用的 `condition` 函数返回 `true`。

`yield` 关键字用于返回当前的 `val`，并可选择接收一个新的种子值 `nextSeed`。`next` 函数用于根据当前的 `val` 和 `nextSeed` 计算下一个值。

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

要使用生成器，请使用 `seed`、`condition` 和 `next` 函数调用它。例如，调用 `[...generateWhile(1, v => v <= 5, v => ++v)]` 将返回 `[1, 2, 3, 4, 5]`。
