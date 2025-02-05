# 代码实践：左子串生成器

要生成给定字符串的所有左子串，请使用下面提供的 `leftSubstrGenerator` 函数。

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

要使用该函数，请打开终端/SSH 并输入 `node`。然后，使用字符串参数输入该函数：

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

如果字符串为空，该函数会使用 `String.prototype.length` 提前终止，并使用带有 `String.prototype.slice()` 的 `for...in` 循环从开头开始 `yield` 给定字符串的每个子串。
