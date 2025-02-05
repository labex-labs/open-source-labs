# CSV 转 JSON

要将逗号分隔值（CSV）字符串转换为对象的二维数组并用于练习编码，请打开终端/SSH 并输入 `node`。字符串的第一行用作标题行。以下是将 CSV 转换为 JSON 的步骤：

1. 使用 `Array.prototype.indexOf()` 找到第一个换行符（`\n`）。
2. 使用 `Array.prototype.slice()` 删除第一行（标题行），并使用提供的 `delimiter` 通过 `String.prototype.split()` 将其拆分为各个值。
3. 使用 `String.prototype.split()` 为每一行创建一个字符串。
4. 使用 `String.prototype.split()` 并根据提供的 `delimiter` 分隔每一行中的值。
5. 使用 `Array.prototype.reduce()` 为每一行的值创建一个对象，其键从标题行解析而来。
6. 省略第二个参数 `delimiter`，以使用默认分隔符 `,`。

以下是代码：

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

要测试该函数，请使用以下示例：

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
