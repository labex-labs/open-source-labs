# 如何替换或追加数组值

要在数组中替换某个项，如果该项不存在则追加它，请按以下步骤操作：

1. 使用展开运算符（`...`）创建数组的浅拷贝。
2. 使用 `Array.prototype.findIndex()` 找到第一个满足提供的比较函数 `compFn` 的元素的索引。
3. 如果未找到这样的元素，则使用 `Array.prototype.push()` 将新值追加到数组中。
4. 否则，使用 `Array.prototype.splice()` 将找到的索引处的值替换为新值。

以下是如何实现此功能的示例：

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

你可以像这样将此函数与对象数组一起使用：

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
