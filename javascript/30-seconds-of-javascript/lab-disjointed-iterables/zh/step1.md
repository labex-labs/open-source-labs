# 检查不相交的可迭代对象

要检查两个可迭代对象是否没有共同的值，可以使用 `isDisjoint` 函数。

使用方法如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Set` 构造函数从每个可迭代对象创建一个新的 `Set` 对象。
3. 使用 `Array.prototype.every()` 和 `Set.prototype.has()` 来检查这两个可迭代对象是否没有共同的值。

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

以下是一些示例：

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
