# JavaScript 에서 숫자를 패딩하는 방법

JavaScript 에서 숫자를 패딩하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 숫자를 문자열로 변환한 후 `String.prototype.padStart()` 메서드를 사용하여 지정된 길이로 숫자를 패딩합니다.
3. 아래의 `padNumber()` 함수는 이 접근 방식을 보여줍니다.
4. 숫자와 원하는 길이를 함수에 인수로 전달합니다.
5. 함수는 패딩된 숫자를 문자열로 반환합니다.

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

사용 예시:

```js
padNumber(1234, 6); // '001234'
```
