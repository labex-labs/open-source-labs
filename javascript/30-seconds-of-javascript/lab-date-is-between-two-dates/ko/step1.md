# 두 날짜 사이에 날짜가 있는지 확인하기

두 날짜 사이에 날짜가 있는지 확인하려면 JavaScript 에서 '보다 큼' (`>`) 및 '보다 작음' (`<`) 연산자를 사용합니다. 다음은 예시 함수입니다.

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

이 함수를 사용하려면 시작 날짜, 종료 날짜 및 확인할 날짜를 전달합니다. 함수는 날짜가 시작 날짜와 종료 날짜 사이에 있으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다. 다음은 몇 가지 예시입니다.

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19)
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25)
); // true
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
