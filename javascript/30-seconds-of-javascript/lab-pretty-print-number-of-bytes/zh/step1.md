# 将字节转换为人类可读的字符串

要将以字节为单位的数字转换为人类可读的字符串，请使用 `prettyBytes()` 函数。请注意以下几点：

- 该函数使用一个单位数组字典，根据指数来访问这些单位。
- 你可以使用第二个参数 `precision` 将数字截断为一定数量的位数。默认值为 `3`。
- 你可以使用第三个参数 `addSpace` 在数字和单位之间添加空格。默认值为 `true`。
- 该函数通过构建字符串来返回美化后的结果，同时会考虑提供的选项以及数字是否为负数。

以下是 `prettyBytes()` 函数的代码：

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

以下是使用 `prettyBytes()` 函数的一些示例：

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
