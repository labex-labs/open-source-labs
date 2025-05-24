# 주어진 날짜에 영업일 추가 함수

주어진 영업일 수를 더하여 미래 날짜를 계산하려면 `addWeekDays` 함수를 사용할 수 있습니다. 다음은 단계별 설명입니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `startDate`와 `count`의 두 인수를 사용하는 `addWeekDays` 함수를 사용합니다.
3. `startDate`는 영업일을 추가하려는 시작 날짜입니다.
4. `count`는 시작 날짜에 추가하려는 영업일 수입니다.
5. 이 함수는 `Array.from()` 메서드를 사용하여 배열을 구성하고 추가할 영업일 수인 `count`와 동일한 길이를 설정합니다.
6. `Array.prototype.reduce()` 메서드는 `startDate`부터 시작하여 `Date.prototype.getDate()` 및 `Date.prototype.setDate()`를 사용하여 증가시키면서 배열을 반복하는 데 사용됩니다.
7. 이 함수는 현재 `date`가 주말인지 여부를 확인합니다.
8. 현재 `date`가 주말인 경우, 함수는 평일로 만들기 위해 하루 또는 이틀을 더하여 다시 업데이트합니다.
9. 이 함수는 공휴일은 고려하지 않습니다.

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

다음은 `addWeekDays` 함수를 사용하는 몇 가지 예입니다.

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
