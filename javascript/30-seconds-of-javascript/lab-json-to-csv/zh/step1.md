# 将 JSON 转换为 CSV

要将对象数组转换为包含指定列的逗号分隔值（CSV）字符串，请使用以下函数：

```js
const JSONtoCSV = (arr, columns, delimiter = ",") =>
  [
    columns.join(delimiter),
    ...arr.map((obj) =>
      columns.reduce(
        (acc, key) =>
          `${acc}${!acc.length ? "" : delimiter}"${!obj[key] ? "" : obj[key]}"`,
        ""
      )
    )
  ].join("\n");
```

要使用它，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用以下参数调用 `JSONtoCSV` 函数：
   - `arr`：要转换的对象数组。
   - `columns`：一个字符串数组，指定要包含在 CSV 输出中的列。
   - `delimiter`：一个可选字符串，指定要使用的分隔符（默认值为 `','`）。
3. 该函数将返回一个 CSV 字符串，其中仅包含指定的列和对象的值。
4. 如果未指定分隔符，则将使用默认分隔符 `','`。
5. 以下代码块中提供了使用该函数的示例。

```js
JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"]
); // 'a,b\n"1","2"\n"3","4"\n"6",""\n"","7"'

JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"],
  ";"
); // 'a;b\n"1";"2"\n"3";"4"\n"6";""\n"";"7"'
```
