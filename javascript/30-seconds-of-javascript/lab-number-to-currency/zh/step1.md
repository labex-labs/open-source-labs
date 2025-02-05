# 数字转换为货币字符串

要将给定数字格式化为货币字符串，请使用 `toCurrency` 函数。此函数接受一个数字和货币代码作为参数，并返回格式化后的字符串。

该函数使用 `Intl.NumberFormat` 来实现特定国家/货币的格式化。你还可以选择传入一种语言格式，用于货币格式化。

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

以下是一些示例：

```js
toCurrency(123456.789, "EUR");
// €123,456.79  | 货币：欧元 | 货币语言格式：本地

toCurrency(123456.789, "USD", "en-us");
// $123,456.79  | 货币：美元 | 货币语言格式：英语（美国）

toCurrency(123456.789, "USD", "fa");
// ۱۲۳٬۴۵۶٫۷۹ ؜$ | 货币：美元 | 货币语言格式：波斯语

toCurrency(322342436423.2435, "JPY");
// ¥322,342,436,423 | 货币：日元 | 货币语言格式：本地

toCurrency(322342436423.2435, "JPY", "fi");
// 322 342 436 423 ¥ | 货币：日元 | 货币语言格式：芬兰语
```
