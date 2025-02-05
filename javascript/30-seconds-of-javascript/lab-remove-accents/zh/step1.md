# 去除重音符号

此函数用于去除字符串中的重音符号。

- 使用 `String.prototype.normalize()` 将字符串转换为规范化的 Unicode 格式。
- 使用 `String.prototype.replace()` 将给定 Unicode 范围内的变音符号替换为空字符串。

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

要使用此函数，请打开终端/SSH 并输入 `node`。然后，以字符串作为参数调用该函数。

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
