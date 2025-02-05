# 检查值是否为类数组

要检查一个值是否为类数组，请执行以下步骤：

1. 打开终端/SSH。
2. 输入 `node`。
3. 使用以下代码检查提供的参数是否可迭代：

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. 如果提供的参数是类数组对象，该函数将返回 `true`，否则返回 `false`。
5. 例如：

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
