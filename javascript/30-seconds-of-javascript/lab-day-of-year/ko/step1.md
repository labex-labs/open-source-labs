# Date 객체를 사용하여 JavaScript 에서 연중 날짜를 구하는 방법

JavaScript 에서 `Date` 객체로부터 연중 날짜 (1-366 사이의 숫자) 를 구하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Date` 생성자와 `Date.prototype.getFullYear()`을 사용하여 연도의 첫 번째 날짜를 `Date` 객체로 가져옵니다.
3. `date` 객체에서 연도의 첫 번째 날짜를 빼고 각 날짜의 밀리초로 나누어 결과를 구합니다.
4. `Math.floor()`를 사용하여 결과 날짜 수를 정수로 반올림합니다.

다음은 코드입니다.

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

함수를 테스트하려면 `Date` 객체를 인수로 사용하여 `dayOfYear()`를 호출합니다.

```js
dayOfYear(new Date()); // 272
```
