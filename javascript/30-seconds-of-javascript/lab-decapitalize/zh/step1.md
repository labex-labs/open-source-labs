# 用于将字符串首字母转换为小写的JavaScript函数

要将字符串的首字母转换为小写，请使用以下JavaScript函数：

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

要使用此函数，请打开终端/SSH并输入 `node`。然后，调用 `decapitalize` 函数，将你想要转换首字母为小写的字符串作为第一个参数传入。

或者，你可以将第二个参数 `upperRest` 设置为 `true`，以将字符串的其余部分转换为大写。如果未提供 `upperRest`，则默认为 `false`。

以下是一些示例：

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
