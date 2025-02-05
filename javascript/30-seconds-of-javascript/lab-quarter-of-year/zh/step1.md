# 确定年份季度的函数

要确定年份的季度，请使用 `quarterOfYear()` 函数。此函数接受一个可选的 `date` 参数，并返回一个数组，其中包含所提供日期所属的季度和年份。

要使用此函数，请打开终端/SSH 并输入 `node`。然后，复制并粘贴以下代码：

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

`quarterOfYear()` 函数使用以下步骤来计算季度和年份：

- 使用 `Date.prototype.getMonth()` 获取当前月份（范围为 0 到 11），加 `1` 将其映射到范围为 1 到 12。
- 使用 `Math.ceil()` 并将月份除以 `3` 以获取当前季度。
- 使用 `Date.prototype.getFullYear()` 从给定的 `date` 中获取年份。
- 省略参数 `date`，默认使用当前日期。

以下是一些使用 `quarterOfYear()` 函数的示例：

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
