# 替换字符串中某个模式最后一次出现的函数

以下是一个用于替换字符串中某个模式最后一次出现位置的函数：

```js
const replaceLast = (str, pattern, replacement) => {
```

要使用它，请打开终端/SSH 并输入 `node`。

- 首先，使用 `typeof` 来确定 `pattern` 是字符串还是正则表达式。
- 如果 `pattern` 是字符串，则将其用作 `match`。
- 否则，使用 `RegExp` 构造函数，根据 `pattern` 的 `RegExp.prototype.source` 创建一个新的正则表达式，并添加 `'g'` 标志。使用 `String.prototype.match()` 和 `Array.prototype.slice()` 获取最后一个匹配项（如果有的话）。

```js
const match =
  typeof pattern === "string"
    ? pattern
    : (str.match(new RegExp(pattern.source, "g")) || []).slice(-1)[0];
```

- 使用 `String.prototype.lastIndexOf()` 找到字符串中匹配项的最后一次出现位置。
- 如果找到匹配项，则使用 `String.prototype.slice()` 和模板字面量将匹配的子字符串替换为给定的 `replacement`。
- 如果未找到匹配项，则返回原始字符串。

```js
  if (!match) return str;
  const last = str.lastIndexOf(match);
  return last!== -1
   ? `${str.slice(0, last)}${replacement}${str.slice(last + match.length)}`
    : str;
};
```

以下是一些使用该函数的示例：

```js
replaceLast("abcabdef", "ab", "gg"); // 'abcggdef'
replaceLast("abcabdef", /ab/, "gg"); // 'abcggdef'
replaceLast("abcabdef", "ad", "gg"); // 'abcabdef'
replaceLast("abcabdef", /ad/, "gg"); // 'abcabdef'
```
