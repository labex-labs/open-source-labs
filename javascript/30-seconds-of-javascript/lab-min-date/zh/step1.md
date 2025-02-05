# 如何在JavaScript中找到最小日期

要在JavaScript中找到最小日期值，可以将ES6展开语法与`Math.min()`和`Date`构造函数一起使用。以下是一个示例代码片段：

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

要使用此函数，创建一个`Date`对象数组，并使用展开语法将其传递给`minDate()`。以下是一个示例：

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // 返回一个表示2016-01-08T22:00:00.000Z的`Date`对象
```

通过使用此代码，你可以轻松地在JavaScript中找到最小日期值。
