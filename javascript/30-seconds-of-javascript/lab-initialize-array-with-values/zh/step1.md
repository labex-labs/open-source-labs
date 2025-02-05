# 使用指定值初始化数组的函数

要开始练习编码，请打开终端/SSH并输入 `node`。

此函数使用指定值初始化数组：

- 使用 `Array()` 构造函数创建所需长度的数组。
- 使用 `Array.prototype.fill()` 用所需值填充它。
- 如果未指定值，则默认值为 `0`。

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

示例用法：

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
