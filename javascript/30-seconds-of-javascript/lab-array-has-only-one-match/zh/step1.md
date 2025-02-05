# 检查数组是否只有一个匹配项的函数

要检查数组是否只有一个值与给定函数匹配，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 将 `Array.prototype.filter()` 与 `fn` 结合使用，以找到所有匹配的数组元素。
3. 使用 `Array.prototype.length` 检查是否只有一个元素与 `fn` 匹配。

以下是代码：

```js
const hasOne = (arr, fn) => arr.filter(fn).length === 1;
```

以下是一个示例：

```js
hasOne([1, 2], (x) => x % 2); // true
hasOne([1, 3], (x) => x % 2); // false
```
