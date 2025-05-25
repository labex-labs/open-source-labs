# 문자열을 제목 대소문자로 변환하는 함수

주어진 문자열을 제목 대소문자 (title case) 로 변환하려면 다음 함수를 사용하십시오. 이 함수는 적절한 정규 표현식 (regular expression) 을 사용하여 문자열을 단어로 분할하기 위해 `String.prototype.match()`를 사용합니다. 그런 다음 `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, 및 `String.prototype.toUpperCase()`를 사용하여 결합합니다. 이 함수는 각 단어의 첫 글자를 대문자로 변환하고 단어 사이에 공백을 추가합니다.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

다음은 이 함수를 사용하는 몇 가지 예입니다.

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
