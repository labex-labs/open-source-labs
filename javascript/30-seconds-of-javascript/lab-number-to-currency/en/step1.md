# Number to Currency String

To format a given number as a currency string, use the `toCurrency` function. This function takes in a number and the currency code as arguments and returns the formatted string.

The function uses `Intl.NumberFormat` to enable country/currency-specific formatting. You can also optionally pass in a language format to be used for the currency formatting.

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

Here are some examples:

```js
toCurrency(123456.789, "EUR");
// €123,456.79  | currency: Euro | currencyLangFormat: Local

toCurrency(123456.789, "USD", "en-us");
// $123,456.79  | currency: US Dollar | currencyLangFormat: English (United States)

toCurrency(123456.789, "USD", "fa");
// ۱۲۳٬۴۵۶٫۷۹ ؜$ | currency: US Dollar | currencyLangFormat: Farsi

toCurrency(322342436423.2435, "JPY");
// ¥322,342,436,423 | currency: Japanese Yen | currencyLangFormat: Local

toCurrency(322342436423.2435, "JPY", "fi");
// 322 342 436 423 ¥ | currency: Japanese Yen | currencyLangFormat: Finnish
```
