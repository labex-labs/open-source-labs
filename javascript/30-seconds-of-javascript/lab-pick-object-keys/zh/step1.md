# 选取对象键的说明

要从对象中选取特定的键值对，请使用函数 `pick(obj, arr)`。

- 将对象作为第一个参数传入，将需要选取的键的数组作为第二个参数传入。
- 该函数返回一个新对象，其中只包含与给定键相对应的键值对。

以下是如何使用 `pick()` 的示例：

```js
const pick = (obj, arr) =>
  arr.reduce((acc, curr) => (curr in obj && (acc[curr] = obj[curr]), acc), {});

pick({ a: 1, b: "2", c: 3 }, ["a", "c"]); // { 'a': 1, 'c': 3 }
```

要开始编码练习，请打开终端/SSH 并输入 `node`。
