# 获取值类型的函数

要获取一个值的类型，请使用以下函数：

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- 如果值为 `undefined` 或 `null`，该函数返回 `'undefined'` 或 `'null'`。
- 否则，它通过使用 `Object.prototype.constructor` 和 `Function.prototype.name` 返回构造函数的名称。

示例用法：

```js
getType(new Set([1, 2, 3])); // 'Set'
```
