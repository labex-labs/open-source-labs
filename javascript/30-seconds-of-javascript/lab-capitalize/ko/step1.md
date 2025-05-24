# 문자열의 첫 글자를 대문자로 변환하는 JavaScript 함수

JavaScript 에서 문자열의 첫 글자를 대문자로 변환하려면 다음 함수를 사용하십시오.

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

이 함수는 배열 분해 (array destructuring) 와 `String.prototype.toUpperCase()`를 사용하여 문자열의 첫 글자를 대문자로 변환합니다. `lowerRest` 인수는 선택 사항이며, 나머지 문자열을 소문자로 변환하려면 `true`로 설정할 수 있습니다.

이 함수를 사용하는 예는 다음과 같습니다.

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
