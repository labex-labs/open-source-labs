# 두 날짜가 동일한지 확인하기

두 날짜가 동일한지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Date.prototype.toISOString()`와 엄격한 동등성 검사 (`===`) 를 사용하여 두 날짜를 비교합니다.
3. 다음은 예시 코드 조각입니다.

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4. 두 날짜를 인수로 사용하여 함수를 테스트하여 동일한지 확인합니다.

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

이 함수는 두 날짜의 ISO 문자열 표현을 비교하여 두 날짜가 동일한지 확인합니다.
