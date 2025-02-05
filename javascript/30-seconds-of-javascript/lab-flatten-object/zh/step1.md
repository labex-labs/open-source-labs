# 扁平化对象

要使用键的路径来扁平化一个对象，请遵循以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用递归来扁平化对象。
3. 使用 `Object.keys()` 并结合 `Array.prototype.reduce()` 将每个叶节点转换为扁平化路径节点。
4. 如果键的值是一个对象，则使用适当的 `prefix` 递归调用该函数，通过 `Object.assign()` 创建路径。
5. 否则，将适当的带前缀的键值对添加到累加器对象中。
6. 省略第二个参数 `prefix`，除非你希望每个键都有一个前缀。

以下是一个示例实现：

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

你可以像这样使用 `flattenObject` 函数：

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
