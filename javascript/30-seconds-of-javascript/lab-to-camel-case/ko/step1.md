# Camelcase 문자열 변환

문자열을 camelCase 로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 적절한 정규 표현식과 함께 `String.prototype.match()`를 사용하여 문자열을 단어로 분리합니다.
3. `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toLowerCase()`, 및 `String.prototype.toUpperCase()`를 사용하여 단어를 결합하고 각 단어의 첫 글자를 대문자로 만듭니다.
4. 아래에 표시된 `toCamelCase` 함수를 사용하여 변환을 수행합니다.

```js
const toCamelCase = (str) => {
  const words =
    str &&
    str.match(
      /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
    );
  const capitalizedWords =
    words &&
    words.map(
      (word) => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase()
    );
  const camelCaseString = capitalizedWords && capitalizedWords.join("");
  return (
    camelCaseString &&
    camelCaseString.slice(0, 1).toLowerCase() + camelCaseString.slice(1)
  );
};
```

`toCamelCase` 함수를 사용하는 몇 가지 예는 다음과 같습니다.

```js
toCamelCase("some_database_field_name"); // 'someDatabaseFieldName'
toCamelCase("Some label that needs to be camelized");
// 'someLabelThatNeedsToBeCamelized'
toCamelCase("some-javascript-property"); // 'someJavascriptProperty'
toCamelCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
