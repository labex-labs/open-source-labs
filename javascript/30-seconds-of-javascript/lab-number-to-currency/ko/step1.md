# 숫자를 통화 문자열로 변환

주어진 숫자를 통화 문자열로 서식 지정하려면 `toCurrency` 함수를 사용하십시오. 이 함수는 숫자와 통화 코드를 인수로 받아 서식 지정된 문자열을 반환합니다.

이 함수는 국가/통화별 서식 지정을 활성화하기 위해 `Intl.NumberFormat`를 사용합니다. 선택적으로 통화 서식 지정에 사용할 언어 형식을 전달할 수도 있습니다.

```js
const toCurrency = (number, currencyCode, languageFormat) =>
  Intl.NumberFormat(languageFormat, {
    style: "currency",
    currency: currencyCode
  }).format(number);
```

다음은 몇 가지 예시입니다.

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
