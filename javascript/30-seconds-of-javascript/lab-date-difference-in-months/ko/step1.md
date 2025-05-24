# 월 단위 날짜 차이 계산 함수

두 날짜 간의 월 단위 차이를 계산하려면 다음 함수를 사용하십시오.

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

이 함수를 사용하려면 두 개의 `Date` 객체를 인수로 전달하십시오. 예를 들어:

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

이 함수는 `Date.prototype.getFullYear()` 및 `Date.prototype.getMonth()` 메서드를 사용하여 두 날짜 간의 월 단위 차이를 계산합니다.
