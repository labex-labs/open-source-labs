# 如何根据函数将数组划分为两个数组

要根据提供的函数将数组划分为两个数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduce()` 创建一个包含两个数组的数组。
3. 使用 `Array.prototype.push()` 将 `fn` 返回 `true` 的元素添加到第一个数组中，并将 `fn` 返回 `false` 的元素添加到第二个数组中。

以下是你可以使用的代码：

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

要测试此代码，你可以使用以下示例：

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

这将返回一个包含两个数组的数组，其中第一个数组包含提供的函数返回 `true` 的所有元素，第二个数组包含提供的函数返回 `false` 的所有元素。
