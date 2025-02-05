# 用于将字符串首字母大写的 JavaScript 函数

要在 JavaScript 中将字符串的首字母大写，请使用以下函数：

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

此函数使用数组解构和 `String.prototype.toUpperCase()` 来将字符串的首字母大写。`lowerRest` 参数是可选的，可以设置为 `true` 以将字符串的其余部分转换为小写。

以下是使用此函数的示例：

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
