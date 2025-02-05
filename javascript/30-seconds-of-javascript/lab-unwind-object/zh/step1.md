# 展开对象函数

要通过对象的数组值属性展开对象，请使用 `unwind` 函数。

- 要开始编码，请打开终端/SSH 并输入 `node`。
- 该函数使用对象解构来从对象中排除指定 `key` 的键值对。
- 然后，它对给定 `key` 的值使用 `Array.prototype.map()` 来创建一个对象数组。
- 每个对象都包含原始对象的值，但 `key` 被映射到其各个值。

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

示例用法：

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
