# Número para String de Moeda

Para formatar um determinado número como uma string de moeda, use a função `toCurrency`. Esta função recebe um número e o código da moeda como argumentos e retorna a string formatada.

A função usa `Intl.NumberFormat` para habilitar a formatação específica de país/moeda. Você também pode, opcionalmente, passar um formato de idioma para ser usado na formatação da moeda.

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

Aqui estão alguns exemplos:

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
