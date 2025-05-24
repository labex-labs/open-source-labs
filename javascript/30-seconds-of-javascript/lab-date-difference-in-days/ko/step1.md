# 날짜 차이 (일) 계산 함수

두 날짜 간의 차이를 일 단위로 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 두 개의 `Date` 객체를 인수로 사용하여 `getDaysDiffBetweenDates` 함수를 사용합니다.
3. 이 함수는 최종 날짜에서 초기 날짜를 빼고 그 결과를 하루의 밀리초 수로 나누어 두 날짜 간의 차이를 일 단위로 구합니다.

다음은 `getDaysDiffBetweenDates` 함수의 코드입니다.

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

함수를 사용하려면 `YYYY-MM-DD` 형식으로 두 개의 `Date` 객체를 전달합니다.

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

이 예제에서는 두 날짜 간의 차이인 9 를 반환합니다.
