# 检查字符串是否为ISO格式

要检查给定字符串是否为简化扩展ISO格式（ISO 8601），请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Date` 构造函数从给定字符串创建一个 `Date` 对象。
3. 使用 `Date.prototype.valueOf()` 和 `Number.isNaN()` 检查生成的日期对象是否有效。
4. 使用 `Date.prototype.toISOString()` 将日期的ISO格式字符串表示与原始字符串进行比较。
5. 如果字符串匹配且日期有效，则返回 `true`。否则，返回 `false`。

以下是一个示例代码片段：

```js
const isISOString = (val) => {
  const d = new Date(val);
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

isISOString("2020-10-12T10:10:10.000Z"); // true
isISOString("2020-10-12"); // false
```

如果字符串是ISO格式，此函数将返回 `true`，否则返回 `false`。
