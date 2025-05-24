# 며칠 전 날짜 계산을 위한 JavaScript 함수

다음은 오늘로부터 `n`일 전의 날짜를 계산하여 `yyyy-mm-dd` 형식의 문자열로 반환하는 JavaScript 함수입니다.

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

작동 방식은 다음과 같습니다.

- `Date` 생성자 (constructor) 를 사용하여 현재 날짜를 가져옵니다.
- `Math.abs()` 함수를 사용하여 며칠 전의 날짜가 양수인지 확인합니다.
- `Date.prototype.getDate()` 함수를 사용하여 현재 날짜의 월별 날짜를 가져옵니다.
- `Date.prototype.setDate()` 함수를 사용하여 날짜를 적절하게 업데이트합니다.
- 결과 날짜는 `Date.prototype.toISOString()` 함수를 사용하여 `yyyy-mm-dd` 형식의 문자열로 반환됩니다.

사용 예시:

```js
daysAgo(20); // "2020-09-16" (현재 날짜가 2020-10-06 인 경우)
```
