# 凯撒密码

要使用凯撒密码，请遵循以下步骤：

1. 打开终端/SSH并输入`node`以开始练习编码。
2. 使用要加密或解密的字符串、偏移值以及一个指示是否解密的布尔值调用`caesarCipher`函数。
3. `caesarCipher`函数使用取模（`%`）运算符和三元运算符（`?`）来计算正确的加密或解密密钥。
4. 它使用展开运算符（`...`）和`Array.prototype.map()`来遍历给定字符串的字母。
5. 它使用`String.prototype.charCodeAt()`和`String.fromCharCode()`来适当地转换每个字母，忽略特殊字符、空格等。
6. 它使用`Array.prototype.join()`将所有字母组合成一个字符串。
7. 如果你想解密一个加密的字符串，在调用`caesarCipher`函数时，将`true`传递给最后一个参数`decrypt`。

以下是`caesarCipher`函数的代码：

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

以下是一些使用`caesarCipher`函数的示例：

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
