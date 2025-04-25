# 如何使用 JavaScript 将字符串哈希为数字

要使用 JavaScript 将输入字符串哈希为一个整数，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`String.prototype.split()`和`Array.prototype.reduce()`方法，利用位运算创建输入字符串的哈希值。
3. 以下是实现哈希算法的`sdbm`函数的代码：

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. 要测试该函数，请使用字符串参数调用它：

```js
sdbm("name"); // -3521204949
```

这将返回输入字符串“name”的哈希值。
