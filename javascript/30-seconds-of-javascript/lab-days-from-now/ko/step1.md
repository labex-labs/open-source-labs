# 오늘로부터 'n'일 후의 날짜를 계산하는 함수

오늘로부터 'n'일 후의 날짜를 계산하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 'node'를 입력하여 코딩 연습을 시작합니다.
- `Date` 생성자를 사용하여 현재 날짜를 가져옵니다.
- `Math.abs()`와 `Date.prototype.getDate()`를 사용하여 날짜를 적절하게 업데이트합니다.
- `Date.prototype.setDate()`를 사용하여 결과를 설정합니다.
- `Date.prototype.toISOString()`를 사용하여 `yyyy-mm-dd` 형식의 문자열을 반환합니다.

다음은 코드입니다.

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

사용 예시:

```js
daysFromNow(5); // Output: 2020-10-13 (if current date is 2020-10-08)
```
