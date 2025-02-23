# Número a Cadena de Moneda

Para formatear un número dado como una cadena de moneda, utiliza la función `toCurrency`. Esta función toma un número y el código de moneda como argumentos y devuelve la cadena formateada.

La función utiliza `Intl.NumberFormat` para habilitar el formateo específico de país/moneda. También puedes pasar opcionalmente un formato de idioma para ser utilizado en el formateo de la moneda.

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

Aquí hay algunos ejemplos:

```js
toCurrency(123456.789, "EUR");
// €123,456.79  | moneda: Euro | formatoIdiomaMoneda: Local

toCurrency(123456.789, "USD", "en-us");
// $123,456.79  | moneda: Dólar estadounidense | formatoIdiomaMoneda: Inglés (Estados Unidos)

toCurrency(123456.789, "USD", "fa");
// ۱۲۳٬۴۵۶٫۷۹ ؜$ | moneda: Dólar estadounidense | formatoIdiomaMoneda: Farsi

toCurrency(322342436423.2435, "JPY");
// ¥322,342,436,423 | moneda: Yen japonés | formatoIdiomaMoneda: Local

toCurrency(322342436423.2435, "JPY", "fi");
// 322 342 436 423 ¥ | moneda: Yen japonés | formatoIdiomaMoneda: Finlandés
```
