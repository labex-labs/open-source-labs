# 查找映射数组交集的说明

要在对两个数组的每个元素都应用一个函数之后找到它们的共同元素，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node`。
2. 使用以下提供的代码：

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. 在代码中，将 `a` 和 `b` 替换为你的数组，并将 `fn` 替换为你要应用于每个元素的函数。
4. 运行代码以获取包含共同元素的结果数组。

示例：

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

在第一个示例中，函数 `Math.floor` 应用于数组 `[2.1, 1.2]` 和 `[2.3, 3.4]`，返回共同元素 `[2.1]`。
在第二个示例中，函数 `x => x.title` 应用于数组 `[{ title: 'Apple' }, { title: 'Orange' }]` 和 `[{ title: 'Orange' }, { title: 'Melon' }]`，返回共同元素 `[{ title: 'Orange' }]`。
