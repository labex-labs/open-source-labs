# 분 단위의 날짜 차이 계산 함수

두 날짜 간의 차이 (분 단위) 를 계산하려면 다음 함수를 사용하십시오.

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

두 `Date` 객체를 빼고 분당 밀리초 수로 나누면 두 객체 간의 차이 (분 단위) 를 얻을 수 있습니다.

다음은 함수의 사용 예시입니다.

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
