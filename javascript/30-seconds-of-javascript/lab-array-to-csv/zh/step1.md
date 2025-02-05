# 将二维数组转换为 CSV

要将二维数组转换为逗号分隔值（CSV）字符串，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.map()` 和 `Array.prototype.join()`，通过提供的 `delimiter` 将各个一维数组（行）组合成字符串。
3. 使用 `Array.prototype.join()` 将所有行组合成一个 CSV 字符串，每行之间用换行符（`\n`）分隔。
4. 如果你想使用默认分隔符 `,`，则省略第二个参数 `delimiter`。

以下是代码示例：

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

你可以通过运行以下代码行来测试该函数：

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
