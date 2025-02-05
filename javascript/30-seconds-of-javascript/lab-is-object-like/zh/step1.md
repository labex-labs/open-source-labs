# 检查一个值是否类似对象

要检查一个值是否类似对象，请执行以下步骤：

1. 打开终端/SSH。
2. 输入 `node` 开始练习编码。
3. 检查提供的值是否不为 `null` 且其 `typeof` 等于 `'object'`。

以下是你可以使用的代码：

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

你可以使用以下示例测试此函数：

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
