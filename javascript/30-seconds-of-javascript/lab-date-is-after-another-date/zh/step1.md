# 如何在JavaScript中检查一个日期是否在另一个日期之后

要在JavaScript中检查一个日期是否在另一个日期之后，可以使用大于运算符（`>`）。以下是一个示例代码片段，用于检查给定日期（`dateA`）是否在另一个日期（`dateB`）之后：

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

要使用此函数，只需传入两个日期对象，如下所示：

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

要尝试此操作，可以打开终端/SSH并输入`node`开始练习编码。
