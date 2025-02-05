# 检查值是否为指定类型的函数

要检查给定的值是否为指定的类型，请执行以下步骤：

- 通过使用 `Array.prototype.includes()` 确保该值不是 `undefined` 或 `null`。
- 使用 `Object.prototype.constructor` 将该值的构造函数属性与指定的 `type` 进行比较。
- 下面的 `is()` 函数执行这些检查，如果该值是指定的类型，则返回 `true`，否则返回 `false`。

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

你可以使用 `is()` 来检查一个值是否为各种类型，如 `Array`、`ArrayBuffer`、`Map`、`RegExp`、`Set`、`WeakMap`、`WeakSet`、`String`、`Number` 和 `Boolean`。例如：

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
