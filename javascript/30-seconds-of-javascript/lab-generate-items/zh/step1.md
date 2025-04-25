# 代码实践

要开始练习编码，请打开终端/SSH 并输入`node`。然后，你可以使用`generateItems`函数生成一个包含特定数量元素的数组。

- 使用所需的元素数量和一个用于生成元素的函数调用`generateItems`。
- `generateItems`使用`Array.from()`创建一个指定长度的空数组，并使用新创建的每个元素的索引调用提供的函数。
- 提供的函数接受一个参数——每个元素的索引。

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

以下是使用`generateItems`生成一个包含 10 个随机数的数组的示例：

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
