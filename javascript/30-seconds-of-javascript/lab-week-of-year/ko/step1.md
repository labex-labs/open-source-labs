# JavaScript 에서 날짜로부터 연도 주차 구하기

JavaScript 에서 날짜에 해당하는 0-인덱스 연도 주차를 구하려면 다음 단계를 따르세요.

1. `date` 매개변수를 받는 `weekOfYear` 함수를 생성합니다.
2. `Date` 생성자와 `Date.prototype.getFullYear()`을 사용하여 해당 연도의 첫 번째 날을 `Date` 객체로 가져옵니다.
3. `Date.prototype.setDate()`, `Date.prototype.getDate()` 및 `Date.prototype.getDay()`을 모듈로 연산자 (`%`) 와 함께 사용하여 해당 연도의 첫 번째 월요일을 구합니다.
4. 주어진 `date`에서 해당 연도의 첫 번째 월요일을 빼고, 주당 밀리초 수로 나눕니다.
5. `Math.round()`를 사용하여 주어진 `date`에 해당하는 0-인덱스 연도 주차를 구합니다.
6. 주어진 `date`가 해당 연도의 첫 번째 월요일보다 이전인 경우, `-0`이 반환됩니다.

다음은 코드입니다.

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

`weekOfYear` 함수를 사용하려면, `Date` 객체를 매개변수로 사용하여 호출하면 됩니다.

```js
weekOfYear(new Date("2021-06-18")); // 23
```

이렇게 하면 주어진 날짜에 해당하는 0-인덱스 연도 주차가 반환되며, 이 경우 `23`입니다.
