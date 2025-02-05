# 使用函数查找数组中的唯一值

要查找数组中的所有唯一值，请提供一个比较函数。

使用 `Array.prototype.reduce()` 和 `Array.prototype.some()` 来创建一个只包含每个值首次唯一出现的数组。比较函数 `fn` 接受两个参数，即正在比较的两个元素的值。

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

要测试该函数，请使用以下示例：

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

通过打开终端/SSH 并输入 `node` 开始练习编码。
