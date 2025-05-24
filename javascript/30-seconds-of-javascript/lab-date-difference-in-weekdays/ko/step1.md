# 두 날짜 사이의 평일 수 계산

두 날짜 사이의 평일 수를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.from()`을 사용하여 `startDate`와 `endDate` 사이의 일수와 동일한 길이를 가진 배열을 생성합니다.
3. `Array.prototype.reduce()`를 사용하여 배열을 반복하고, 각 날짜가 평일인지 확인하여 `count`를 증가시킵니다.
4. `Date.prototype.getDate()` 및 `Date.prototype.setDate()`를 사용하여 각 루프에서 `startDate`를 다음 날짜로 업데이트하여 하루씩 진행합니다.
5. 이 함수는 공휴일을 고려하지 않는다는 점에 유의하십시오.

다음은 이를 구현하는 코드입니다.

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

다음 코드를 사용하여 함수를 테스트할 수 있습니다.

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
