# 如何在 JavaScript 中检查一个日期是否在另一个日期之前

要在 JavaScript 中检查一个日期是否在另一个日期之前，可以使用小于运算符（`<`）。下面是一个示例函数，它接受两个日期并返回一个布尔值，指示第一个日期是否在第二个日期之前：

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

通过将两个 `Date` 对象作为参数传入，可以使用此函数检查特定日期是否在另一个日期之前。例如：

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
