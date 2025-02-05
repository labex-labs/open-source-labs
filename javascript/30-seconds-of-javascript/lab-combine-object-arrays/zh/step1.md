# 基于指定键合并对象数组的函数

要基于特定键合并两个对象数组，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduce()` 和一个对象累加器，根据给定的 `prop` 合并两个数组中的所有对象。
3. 使用 `Object.values()` 将结果对象转换为数组并返回。

以下是你可以使用的函数：

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

以下是如何使用此函数的示例：

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
