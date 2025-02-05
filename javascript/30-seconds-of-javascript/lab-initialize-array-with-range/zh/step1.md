# 使用范围初始化数组的函数

要使用一系列数字初始化数组，请使用以下函数：

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

此函数接受三个参数：`end`（必填）、`start`（可选，默认值为`0`）和`step`（可选，默认值为`1`）。它返回一个包含指定范围内数字的数组，其中`start`和`end`包含在它们的公差`step`中。

要使用此函数，只需使用所需的范围参数调用它：

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

此函数使用`Array.from()`创建所需长度的数组，然后使用映射函数在给定范围内用所需值填充数组。如果你省略第二个参数`start`，它将使用默认值`0`。如果你省略最后一个参数`step`，它将使用默认值`1`。
