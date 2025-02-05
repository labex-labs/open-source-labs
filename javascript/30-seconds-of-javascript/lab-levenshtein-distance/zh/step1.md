# 莱文斯坦距离算法

要计算两个字符串之间的差异，你可以使用莱文斯坦距离算法。具体做法如下：

1. 如果任一字符串的 `length` 为零，则返回另一个字符串的 `length`。
2. 使用嵌套的 `for` 循环遍历目标字符串和源字符串的各个字符。
3. 分别计算在目标字符串和源字符串中替换对应于 `i - 1` 和 `j - 1` 的字符的成本（如果它们相同则为 `0`，否则为 `1`）。
4. 使用 `Math.min()` 用以下三者中的最小值填充二维数组中的每个元素：上方单元格的值加一、左侧单元格的值加一、左上角单元格的值加上先前计算的成本。
5. 返回生成数组最后一行的最后一个元素。

要开始练习这段代码，打开终端/SSH 并输入 `node`。以下是你可以使用的代码：

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
