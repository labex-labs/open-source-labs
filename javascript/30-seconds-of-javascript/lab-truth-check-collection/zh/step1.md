# 真值检查集合函数

要练习编码，请在终端/SSH 中输入 `node`。

以下是一个函数，用于检查谓词函数对集合中的所有元素是否都为真值。

- 使用 `Array.prototype.every()` 检查每个传入的对象是否具有指定的属性，以及它是否返回真值。

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

示例用法：

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
