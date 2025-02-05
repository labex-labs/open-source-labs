# 在数组中查找反转后的唯一值的函数

要根据从右到左提供的比较函数来查找数组的所有唯一值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduceRight()` 和 `Array.prototype.some()` 根据比较函数 `fn` 创建一个只包含每个值最后一次唯一出现的数组。
3. 比较函数接受两个参数：正在比较的两个元素的值。
4. 以下是实现该函数的代码：

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. 使用以下代码测试该函数：

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
