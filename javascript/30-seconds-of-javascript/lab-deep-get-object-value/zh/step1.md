# 如何使用键数组在对象中检索嵌套值

要从嵌套的 JSON 对象中检索特定值，可以使用 `deepGet` 函数。该函数接受一个对象和一个键数组，如果目标值存在于对象中，则返回该值。

要使用 `deepGet` 函数：

- 创建一个你想要从嵌套 JSON 对象中检索的键的数组。
- 使用对象和键数组调用 `deepGet` 函数。
- 如果目标值存在，该函数将返回它；如果不存在，则返回 `null`。

以下是 `deepGet` 函数的代码：

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

以下是如何使用 `deepGet` 函数的示例：

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // 返回 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // 返回 null
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
