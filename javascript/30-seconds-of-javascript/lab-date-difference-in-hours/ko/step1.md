# JavaScript 함수를 사용하여 시간 단위의 날짜 차이 계산하기

JavaScript 를 사용하여 두 날짜 간의 시간 차이를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. 두 `Date` 객체 간의 차이 (시간 단위) 를 얻으려면 다음 JavaScript 함수를 사용합니다.

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. 두 날짜를 인수로 사용하여 함수를 호출하여 시간 단위의 차이를 얻습니다.

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
