# 检查两个日期是否相同

要检查两个日期是否相同，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Date.prototype.toISOString()` 和严格相等性检查 (`===`) 来比较这两个日期。
3. 以下是一个示例代码片段：

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4. 使用两个日期作为参数测试该函数，以查看它们是否相同：

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

此函数通过比较两个日期的ISO字符串表示形式来检查它们是否相同。
