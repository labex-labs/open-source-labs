# 如何在JavaScript中深度合并对象

要在JavaScript中深度合并两个对象，你可以使用 `deepMerge` 函数。该函数接受两个对象和一个函数作为参数。这个函数用于处理两个对象中都存在的键。

以下是 `deepMerge` 函数的工作原理：

1. 使用 `Object.keys()` 获取两个对象的键，从它们创建一个 `Set`，并使用展开运算符 (`...`) 创建一个包含所有唯一键的数组。
2. 使用 `Array.prototype.reduce()` 将每个唯一键添加到对象中，使用 `fn` 来合并两个给定对象的值。

以下是 `deepMerge` 函数的代码：

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

要使用 `deepMerge` 函数，用两个对象和一个函数调用它。以下是一个示例：

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

在这个示例中，`deepMerge` 函数用于合并两个对象。结果对象包含了两个对象合并后的值。
