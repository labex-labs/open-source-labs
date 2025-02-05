# 查找最大日期

要从给定的日期数组中找到最大日期值，请执行以下步骤：

1. 打开终端或 SSH。
2. 输入 `node` 开始练习编码。
3. 使用 ES6 展开语法与 `Math.max()` 来查找最大日期值。
4. 使用 `Date` 构造函数将最大日期值转换为 `Date` 对象。

以下是一个示例代码片段：

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // 返回 "2018-03-11T22:00:00.000Z"
```

通过遵循这些步骤并使用提供的代码，你可以轻松地从给定的日期数组中找到最大日期值。
