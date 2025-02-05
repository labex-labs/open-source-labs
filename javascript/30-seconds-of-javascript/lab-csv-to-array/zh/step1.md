# 将 CSV 转换为数组

要将逗号分隔值（CSV）字符串转换为二维数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始编码。
2. 使用 `Array.prototype.indexOf()` 定位第一个换行符（`\n`）。
3. 如果 `omitFirstRow` 设置为 `true`，则使用 `Array.prototype.slice()` 删除第一行（标题行）。
4. 使用 `String.prototype.split()` 为每一行创建一个字符串。
5. 使用 `String.prototype.split()` 使用提供的 `delimiter` 分隔每一行中的值。
6. 如果你不提供第二个参数 `delimiter`，将使用默认分隔符 `','`。
7. 如果你不提供第三个参数 `omitFirstRow`，CSV 字符串的第一行（标题行）将被包含在内。

以下是将 CSV 转换为数组的代码：

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

你可以使用以下示例测试该函数：

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
