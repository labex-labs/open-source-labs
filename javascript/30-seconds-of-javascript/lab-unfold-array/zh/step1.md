# 展开数组

要使用迭代器函数和初始种子值创建数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `while` 循环和 `Array.prototype.push()` 反复调用迭代器函数，直到它返回 `false`。
3. 迭代器函数应接受一个参数（`seed`），并始终返回一个包含两个元素的数组（`[value, nextSeed]`）或 `false` 以终止。

使用以下代码实现 `unfold` 函数：

```js
const unfold = (fn, seed) => {
  let result = [],
    val = [null, seed];
  while ((val = fn(val[1]))) result.push(val[0]);
  return result;
};
```

以下是如何使用 `unfold` 函数的示例：

```js
var f = (n) => (n > 50 ? false : [-n, n + 10]);
unfold(f, 10); // [-10, -20, -30, -40, -50]
```

这将生成一个数组，其中的值由迭代器函数 `f` 从初始种子值 `10` 开始生成。迭代器函数在每一步生成一个包含两个元素的数组：当前种子值的相反数和下一个种子值，下一个种子值递增 `10`。这个过程会一直持续，直到种子值大于 `50`，此时函数返回 `false`。
