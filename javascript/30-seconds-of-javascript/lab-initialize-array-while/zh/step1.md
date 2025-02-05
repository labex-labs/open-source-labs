# 如何在 JavaScript 中使用 while 循环初始化并填充数组

要开始练习 JavaScript 编码，请打开终端/SSH 并输入 `node`。

`initializeArrayWhile` 函数会在满足某个条件时，使用一个函数生成的值来初始化并填充数组。其工作原理如下：

1. 创建一个名为 `arr` 的空数组、一个名为 `i` 的索引变量以及一个名为 `el` 的元素。
2. 使用 `while` 循环，只要 `conditionFn` 函数针对给定的索引 `i` 和元素 `el` 返回 `true`，就使用 `mapFn` 函数将元素添加到数组中。
3. `conditionFn` 函数接受三个参数：当前索引、前一个元素以及数组本身。
4. `mapFn` 函数接受三个参数：当前索引、当前元素以及数组本身。
5. `initializeArrayWhile` 函数返回该数组。

以下是代码：

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

你可以使用 `initializeArrayWhile` 函数来初始化并填充数组。例如：

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
