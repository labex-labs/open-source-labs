# 如何检查日期是否有效

要检查一个日期是否有效，请遵循以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用展开运算符（`...`）将参数数组传递给 `Date` 构造函数。
3. 使用 `Date.prototype.valueOf()` 和 `Number.isNaN()` 来检查是否可以根据给定值创建有效的 `Date` 对象。

以下是一个示例代码片段：

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

你可以使用不同的值来测试该函数，如下所示：

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
