# 字符串排列算法

要生成包含重复项的字符串的所有排列，请使用以下算法：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用递归创建给定字符串的所有可能排列。
3. 对于给定字符串中的每个字母，为其余字母创建所有部分排列。
4. 使用 `Array.prototype.map()` 将该字母与每个部分排列组合。
5. 使用 `Array.prototype.reduce()` 将所有排列合并到一个数组中。
6. 基本情况是 `String.prototype.length` 等于 `2` 或 `1`。
7. ⚠️ **警告**：执行时间会随着每个字符呈指数级增长。对于长度超过 8 到 10 个字符的字符串，环境可能会在尝试解决所有不同组合时挂起。

以下是该算法的 JavaScript 代码：

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

你可以使用以下代码测试 `stringPermutations` 函数：

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
