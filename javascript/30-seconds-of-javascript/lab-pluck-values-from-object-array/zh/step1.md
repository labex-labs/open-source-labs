# 从对象数组中提取值的说明

要从对象数组中提取值，你可以按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.map()` 将对象数组映射到每个对象的指定 `key` 的值。
3. 实现以下函数：

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. 使用一个示例对象数组测试该函数：

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

这将返回一个与对象数组中指定 `key` 相对应的值数组。
