# 基于函数过滤数组中的唯一值

以下是如何通过基于比较函数 `fn` 过滤掉唯一值来创建一个只包含非唯一值的数组：

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

要使用此函数，请使用两个参数调用 `filterUniqueBy()`：要过滤的数组和比较函数。比较函数应接受四个参数：正在比较的两个元素的值及其索引。

例如，如果你有一个对象数组，并且想要过滤掉具有唯一 `id` 值的对象，可以这样做：

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
