# 遍历对象键

要生成给定对象的所有键的列表，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。

2. 定义一个名为 `walk` 的生成器函数，它接受一个对象和一个键数组。使用递归来遍历对象的所有键。

3. 在 `walk` 函数内部，使用 `for...of` 循环和 `Object.keys()` 来迭代对象的键。

4. 使用 `typeof` 检查给定对象中的每个值本身是否为对象。如果该值是对象，则使用 `yield*` 表达式递归地委托给同一个生成器函数 `walk`，将当前的 `key` 添加到键数组中。

5. 否则，`yield` 一个表示当前路径的键数组和给定 `key` 的值。

6. 使用 `yield*` 表达式委托给 `walk` 生成器函数。

以下是代码：

```js
const walkThrough = function* (obj) {
  const walk = function* (x, previous = []) {
    for (let key of Object.keys(x)) {
      if (typeof x[key] === "object") yield* walk(x[key], [...previous, key]);
      else yield [[...previous, key], x[key]];
    }
  };
  yield* walk(obj);
};
```

要测试代码，请创建一个对象并使用 `walkThrough` 函数生成其所有键的列表：

```js
const obj = {
  a: 10,
  b: 20,
  c: {
    d: 10,
    e: 20,
    f: [30, 40]
  },
  g: [
    {
      h: 10,
      i: 20
    },
    {
      j: 30
    },
    40
  ]
};
[...walkThrough(obj)];
/*
[
  [['a'], 10],
  [['b'], 20],
  [['c', 'd'], 10],
  [['c', 'e'], 20],
  [['c', 'f', '0'], 30],
  [['c', 'f', '1'], 40],
  [['g', '0', 'h'], 10],
  [['g', '0', 'i'], 20],
  [['g', '1', 'j'], 30],
  [['g', '2'], 40]
]
*/
```
