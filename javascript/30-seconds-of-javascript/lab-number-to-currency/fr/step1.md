# Nombre en chaîne de caractères de devise

Pour formater un nombre donné en chaîne de caractères de devise, utilisez la fonction `toCurrency`. Cette fonction prend un nombre et le code de la devise en arguments et renvoie la chaîne de caractères formatée.

La fonction utilise `Intl.NumberFormat` pour activer la mise en forme spécifique au pays/devise. Vous pouvez également passer facultativement un format de langue à utiliser pour la mise en forme de la devise.

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

Voici quelques exemples :

```js
toCurrency(123456.789, "EUR");
// €123,456.79  | devise: Euro | formatLangDevise: Local

toCurrency(123456.789, "USD", "en-us");
// $123,456.79  | devise: Dollar américain | formatLangDevise: Anglais (États-Unis)

toCurrency(123456.789, "USD", "fa");
// ۱۲۳٬۴۵۶٫۷۹ ؜$ | devise: Dollar américain | formatLangDevise: Persan

toCurrency(322342436423.2435, "JPY");
// ¥322,342,436,423 | devise: Yen japonais | formatLangDevise: Local

toCurrency(322342436423.2435, "JPY", "fi");
// 322 342 436 423 ¥ | devise: Yen japonais | formatLangDevise: Finnois
```
