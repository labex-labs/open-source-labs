# 如何在 JavaScript 中将数组映射为对象

要在 JavaScript 中将对象数组映射为对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduce()` 将数组映射为对象。
3. 使用 `mapKey` 参数映射对象的键，并使用 `mapValue` 参数映射值。

以下是一个示例代码片段，展示了如何使用 `objectify` 函数将对象数组映射为对象：

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

然后，你可以使用 `objectify` 函数以以下方式将对象数组映射为对象：

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// 使用 name 属性作为键将对象数组映射为对象
objectify(people, (p) => p.name.toLowerCase());
// 输出: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// 使用 name 属性作为键，age 属性作为值将对象数组映射为对象
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// 输出: { john: 42, adam: 39 }
```
