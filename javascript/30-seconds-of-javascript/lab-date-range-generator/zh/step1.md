# 日期范围生成器

要使用给定的步长生成给定范围内的所有日期，请在终端/SSH 中使用以下代码并输入 `node`：

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

这创建了一个生成器，它使用 `while` 循环从 `start` 迭代到 `end`，使用 `Date` 构造函数返回范围内的每个日期，并使用 `Date.prototype.getDate()` 和 `Date.prototype.setDate()` 按 `step` 天递增。

要将 `step` 的默认值设为 `1`，请省略第三个参数。

以下是使用 `dateRangeGenerator` 的示例：

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
