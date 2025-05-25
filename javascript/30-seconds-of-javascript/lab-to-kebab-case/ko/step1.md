# 문자열을 케밥 케이스로 변환하기

문자열을 케밥 케이스로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 적절한 정규 표현식 (regular expression) 을 사용하여 `String.prototype.match()`를 사용하여 문자열을 단어로 분리합니다.
3. `Array.prototype.map()`, `Array.prototype.join()`, 및 `String.prototype.toLowerCase()`를 사용하여 단어를 결합하고 구분 기호로 `-`를 추가합니다.

다음은 변환을 수행하는 예시 함수입니다.

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

아래와 같이 이 함수를 사용하여 문자열을 케밥 케이스로 변환할 수 있습니다.

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); // 'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
