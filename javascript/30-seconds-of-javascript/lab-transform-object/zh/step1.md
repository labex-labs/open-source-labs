# 对象转换

要开始练习编码，请打开终端/SSH 并输入 `node`。

`transform` 函数会从左到右对累加器和对象中的每个键应用指定的函数。以下是使用方法：

- 使用 `Object.keys()` 遍历对象中的每个键。
- 使用 `Array.prototype.reduce()` 对给定的累加器应用指定的函数。

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

以下是一个示例：

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
