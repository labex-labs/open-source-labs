# JavaScript 에서 Non-ASCII 문자 제거 방법

JavaScript 에서 인쇄 불가능한 ASCII 문자를 제거하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 정규 표현식과 함께 `String.prototype.replace()` 메서드를 사용하여 인쇄 불가능한 ASCII 문자를 제거합니다.
3. 정규 표현식 `/[^\x20-\x7E]/g`는 인쇄 가능한 ASCII 범위 (10 진수 값 32~126) 에 없는 모든 문자를 일치시킵니다.
4. `g` 플래그는 전역 일치 (즉, 문자열에서 non-ASCII 문자의 모든 발생을 대체) 를 수행하는 데 사용됩니다.
5. `removeNonASCII` 함수를 사용하는 방법의 예는 다음과 같습니다.

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

이렇게 하면 모든 non-ASCII 문자가 제거된 문자열이 반환됩니다.
