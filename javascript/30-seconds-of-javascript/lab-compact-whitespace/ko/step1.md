# 문자열 내 공백 압축 함수

문자열 내 공백을 압축하려면 `compactWhitespace()` 함수를 사용하십시오.

- 이 함수는 `String.prototype.replace()`를 정규 표현식 (regular expression) 과 함께 사용하여 두 개 이상의 공백 문자가 나타나는 모든 경우를 단일 공백으로 대체합니다.
- 이 함수는 문자열을 인수로 받아 압축된 문자열을 반환합니다.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

사용 예시:

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
