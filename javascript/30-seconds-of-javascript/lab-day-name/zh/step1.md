# 从日期对象中获取星期名称

要从 `Date` 对象中获取星期几的名称，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用带有 `{ weekday: 'long' }` 选项的 `Date.prototype.toLocaleDateString()` 来获取星期几。
3. 你可以使用可选的第二个参数来获取特定语言的名称，或者省略它以使用默认语言环境。

以下是一个示例实现：

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

你可以像这样使用此函数：

```js
dayName(new Date()); // '星期六'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
