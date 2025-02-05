# 如何在满足条件前初始化数组

要开始练习编码，请打开终端/SSH 并输入 `node`。

以下是使用函数生成的值初始化和填充数组，直到满足特定条件的步骤：

1. 创建一个空数组 `arr`、一个索引变量 `i` 和一个元素 `el`。
2. 使用 `do...while` 循环，通过 `mapFn` 函数将元素添加到数组中，直到 `conditionFn` 函数针对给定的索引 `i` 和元素 `el` 返回 `true`。
3. `conditionFn` 函数接受三个参数：当前索引、前一个元素和数组本身。
4. `mapFn` 函数接受三个参数：当前索引、当前元素和数组本身。

以下是代码：

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

要使用 `initializeArrayUntil` 函数，请提供两个函数作为参数：

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

这段代码使用斐波那契数列初始化一个数组，直到第一个大于 10 的数字。`conditionFn` 函数检查当前值是否大于 10，`mapFn` 函数生成序列中的下一个数字。
