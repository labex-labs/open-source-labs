# 以下是对字符串中的字符进行排序的方法：

使用以下代码按字母顺序对字符串中的字符进行排序：

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

首先，打开终端/SSH 并输入 `node` 开始练习编码。

示例用法：

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
