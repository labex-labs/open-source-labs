# Zahl in Währungsstring

Um eine gegebene Zahl als Währungsstring zu formatieren, verwenden Sie die `toCurrency`-Funktion. Diese Funktion nimmt eine Zahl und den Währungscode als Argumente entgegen und gibt den formatierten String zurück.

Die Funktion verwendet `Intl.NumberFormat`, um eine landesspezifische/Währungsformatierung zu ermöglichen. Optionaler können Sie auch einen Sprachformatierungsstring übergeben, der für die Währungsformatierung verwendet werden soll.

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

Hier sind einige Beispiele:

```js
toCurrency(123456.789, "EUR");
// €123.456,79  | currency: Euro | currencyLangFormat: Local

toCurrency(123456.789, "USD", "en-us");
// $123.456,79  | currency: US Dollar | currencyLangFormat: Englisch (Vereinigte Staaten)

toCurrency(123456.789, "USD", "fa");
// ۱۲۳٬۴۵۶٫۷۹ ؜$ | currency: US Dollar | currencyLangFormat: Farsi

toCurrency(322342436423.2435, "JPY");
// ¥322.342.436.423 | currency: Japanischer Yen | currencyLangFormat: Local

toCurrency(322342436423.2435, "JPY", "fi");
// 322 342 436 423 ¥ | currency: Japanischer Yen | currencyLangFormat: Finnisch
```
