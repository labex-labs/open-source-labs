# 날짜 객체에서 요일 이름 가져오기

`Date` 객체에서 요일 이름을 가져오려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `{ weekday: 'long' }` 옵션과 함께 `Date.prototype.toLocaleDateString()`을 사용하여 요일을 가져옵니다.
3. 선택적 두 번째 인수를 사용하여 언어별 이름을 가져오거나, 생략하여 기본 로케일을 사용할 수 있습니다.

다음은 예시 구현입니다.

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

이 함수는 다음과 같이 사용할 수 있습니다.

```js
dayName(new Date()); // 'Saturday'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
