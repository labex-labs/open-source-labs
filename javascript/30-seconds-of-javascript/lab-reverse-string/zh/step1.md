# 以下是一个用于反转字符串的函数：

要反转字符串，请使用展开运算符（`...`）和 `Array.prototype.reverse()`。使用 `Array.prototype.join()` 将字符组合成一个字符串。以下是代码：

```js
const reverseString = (str) => [...str].reverse().join("");
```

示例用法：

```js
reverseString("foobar"); // 'raboof'
```
