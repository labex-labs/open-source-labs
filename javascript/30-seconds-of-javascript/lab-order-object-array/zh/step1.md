# 如何在 JavaScript 中对对象数组进行排序

要在 JavaScript 中对对象数组进行排序，你可以在 `props` 数组上使用 `Array.prototype.sort()` 方法和 `Array.prototype.reduce()` 方法，并使用默认值 `0`。

以下是一个示例函数 `orderBy`，它根据指定的属性和顺序对对象数组进行排序：

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

要使用此函数，请传入一个对象数组、一个要排序的属性数组以及一个可选的顺序数组。如果未提供 `orders` 数组，函数将默认按 `'asc'` 排序。

以下是一些使用 `orderBy` 函数的示例：

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// 按名字升序和年龄降序排序
orderBy(users, ["name", "age"], ["asc", "desc"]);
// 输出：[{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// 按名字升序和年龄升序排序（默认顺序）
orderBy(users, ["name", "age"]);
// 输出：[{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
