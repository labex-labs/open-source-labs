# 날짜 유효성 검사 방법

날짜가 유효한지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. spread operator (`...`) 를 사용하여 인수의 배열을 `Date` 생성자에 전달합니다.
3. `Date.prototype.valueOf()` 및 `Number.isNaN()`을 사용하여 주어진 값에서 유효한 `Date` 객체를 생성할 수 있는지 확인합니다.

다음은 예시 코드 조각입니다.

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

아래와 같이 다양한 값으로 함수를 테스트할 수 있습니다.

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
