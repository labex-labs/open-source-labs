# 数値を通貨形式の文字列に変換する

与えられた数値を通貨形式の文字列にフォーマットするには、`toCurrency` 関数を使用します。この関数は、数値と通貨コードを引数として受け取り、フォーマットされた文字列を返します。

この関数は、特定の国や通貨に応じたフォーマットを可能にするために `Intl.NumberFormat` を使用します。また、通貨フォーマットに使用する言語形式を任意で指定することもできます。

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

以下はいくつかの例です。

```js
toCurrency(123456.789, "EUR");
// €123,456.79  | 通貨: ユーロ | 通貨言語形式: ローカル

toCurrency(123456.789, "USD", "en-us");
// $123,456.79  | 通貨: 米ドル | 通貨言語形式: 英語（アメリカ合衆国）

toCurrency(123456.789, "USD", "fa");
// ۱۲۳٬۴۵۶٫۷۹ ؜$ | 通貨: 米ドル | 通貨言語形式: ペルシャ語

toCurrency(322342436423.2435, "JPY");
// ¥322,342,436,423 | 通貨: 日本円 | 通貨言語形式: ローカル

toCurrency(322342436423.2435, "JPY", "fi");
// 322 342 436 423 ¥ | 通貨: 日本円 | 通貨言語形式: フィンランド語
```
