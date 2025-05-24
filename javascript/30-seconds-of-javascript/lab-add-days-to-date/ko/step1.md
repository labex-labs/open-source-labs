# 날짜에 며칠 더하는 함수

다음은 주어진 날짜로부터 `n`일 후의 날짜를 계산하고 문자열 표현으로 반환하는 함수입니다.

이 함수를 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Date` 생성자를 사용하여 첫 번째 인자로부터 `Date` 객체를 생성합니다.
3. `Date.prototype.getDate()`와 `Date.prototype.setDate()`를 사용하여 주어진 날짜에 `n`일을 더합니다.
4. `Date.prototype.toISOString()`를 사용하여 `yyyy-mm-dd` 형식의 문자열을 반환합니다.

다음은 함수의 코드입니다.

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
