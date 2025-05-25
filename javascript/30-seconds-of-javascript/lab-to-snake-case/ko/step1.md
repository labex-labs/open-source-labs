# 문자열을 Snake Case 로 변환하는 함수

문자열을 snake case 로 변환하려면 다음 함수를 사용하십시오.

```js
const toSnakeCase = (str) => {
  if (!str) return "";
  const regex =
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
  return str
    .match(regex)
    .map((x) => x.toLowerCase())
    .join("_");
};
```

이 함수는 적절한 정규 표현식을 사용하여 문자열을 단어로 분해하기 위해 `String.prototype.match()`를 사용합니다. 그런 다음 `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, 그리고 `String.prototype.toLowerCase()`를 사용하여 단어를 결합하고 `_`를 구분 기호로 추가합니다.

사용 예시:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); // 'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
