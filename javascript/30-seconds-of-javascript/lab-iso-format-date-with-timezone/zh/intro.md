# 简介

在本实验中，我们将学习如何将日期转换为扩展的 ISO 格式（ISO 8601），包括时区偏移。我们将使用 `Date.prototype.getTimezoneOffset()` 方法获取时区偏移并将其反转。然后，我们将定义一个辅助函数，将任何传入的数字规范化为整数，并使用 `String.prototype.padStart()` 将其填充为两位数。最后，我们将使用 `Date` 原型中的内置方法来构建带有时区偏移的 ISO 8601 字符串。在本实验结束时，你将对如何在 JavaScript 中操作日期有更深入的理解。
