# 精简对象算法

要从对象或数组中深度移除所有虚假值，请使用以下算法：

1. 使用递归对每个嵌套的对象或数组调用 `compactObject()` 函数。
2. 使用 `Array.isArray()`、`Array.prototype.filter()` 和 `Boolean()` 初始化可迭代数据。这样做是为了避免稀疏数组。
3. 使用 `Object.keys()` 和 `Array.prototype.reduce()` 以适当的初始值遍历每个键。
4. 使用 `Boolean()` 确定每个键值的真值性，如果为真值则将其添加到累加器中。
5. 使用 `typeof` 确定给定值是否为 `object`，并再次调用该函数以深度精简它。

以下是 `compactObject()` 函数的代码：

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

要使用此函数，将对象或数组作为参数传递给 `compactObject()`。该函数将返回一个移除了所有虚假值的新对象或数组。

例如：

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
