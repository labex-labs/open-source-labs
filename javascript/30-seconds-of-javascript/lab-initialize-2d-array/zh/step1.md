# 在JavaScript中初始化二维数组

要在JavaScript中初始化二维数组，你可以使用以下代码：

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

这段代码使用 `Array.from()` 和 `Array.prototype.map()` 创建一个包含 `height` 行的数组，其中每行都是一个长度为 `width` 的新数组。它还使用 `Array.prototype.fill()` 将数组中的所有元素设置为 `value` 参数。如果未提供 `value`，则默认值为 `null`。

你可以像这样调用该函数：

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

这将创建一个宽度为2、高度为2且所有值都设置为0的二维数组。
