# 최대 날짜 찾기

주어진 날짜 배열에서 최대 날짜 값을 찾으려면 다음 단계를 따르세요:

1. 터미널 (Terminal) 또는 SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. `Math.max()`와 함께 ES6 스프레드 구문 (spread syntax) 을 사용하여 최대 날짜 값을 찾습니다.
4. `Date` 생성자를 사용하여 최대 날짜 값을 `Date` 객체로 변환합니다.

다음은 예시 코드 조각입니다:

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Returns "2018-03-11T22:00:00.000Z"
```

이러한 단계를 따르고 제공된 코드를 사용하면 주어진 날짜 배열에서 최대 날짜 값을 쉽게 찾을 수 있습니다.
