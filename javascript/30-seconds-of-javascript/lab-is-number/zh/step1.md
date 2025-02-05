# 在JavaScript中检查一个值是否为数字

要在JavaScript中检查一个值是否为数字，可以使用 `typeof` 运算符来确定该值是否被归类为数字原始类型。为了防止与 `NaN` 相关的问题（`NaN` 的 `typeof` 等于 `number` 且不等于自身），还可以使用 `val === val` 来检查该值是否等于自身。

以下是一个检查给定值是否为数字的示例函数：

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

你可以像这样使用这个函数：

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
