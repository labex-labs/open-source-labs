# 如何根据属性顺序对对象数组进行排序

要根据属性顺序对对象数组进行排序，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()` 从 `order` 数组创建一个对象，将值作为键，其原始索引作为值。
3. 使用 `Array.prototype.sort()` 对给定数组进行排序，跳过 `prop` 为空或不在 `order` 数组中的元素。

以下是一个根据属性顺序对对象数组进行排序的示例代码片段：

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

你可以使用 `orderWith` 函数根据属性顺序对对象数组进行排序。例如：

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
