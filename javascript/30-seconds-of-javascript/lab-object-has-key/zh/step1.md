# 用于检查对象是否有键的 JavaScript 函数

要检查目标值是否存在于 JavaScript 对象中，请使用 `hasKey` 函数。

该函数接受两个参数：`obj`，要在其中搜索的 JSON 对象，以及 `keys`，要检查的键数组。以下是检查对象是否具有给定键的步骤：

1. 检查 `keys` 数组是否非空。如果为空，则返回 `false`。
2. 使用 `Array.prototype.every()` 方法遍历 `keys` 数组，并依次检查每个键到 `obj` 的内部深度。
3. 使用 `Object.prototype.hasOwnProperty()` 方法检查 `obj` 是否没有当前键或不是一个对象。如果这些条件中的任何一个为真，则停止传播并返回 `false`。
4. 否则，将键的值赋给 `obj` 以供下一次迭代使用。
5. 如果成功遍历了 `keys` 数组，则返回 `true`。

以下是 `hasKey` 函数的代码：

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

以下是一些使用 `hasKey` 函数的示例：

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
