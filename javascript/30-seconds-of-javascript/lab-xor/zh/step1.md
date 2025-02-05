# 逻辑异或

要开始练习编码，请打开终端/SSH 并输入 `node`。逻辑异或用于检查两个参数中是否只有一个为 `true`。要创建逻辑异或，可以对两个给定值使用逻辑或（`||`）、与（`&&`）和非（`!`）运算符。以下是实现此功能的示例代码：

```js
const xor = (a, b) => (a || b) && !(a && b);
```

以下是输出值：

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
