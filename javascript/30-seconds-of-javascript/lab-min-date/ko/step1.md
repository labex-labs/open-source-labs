# JavaScript 에서 최소 날짜 찾기

JavaScript 에서 최소 날짜 값을 찾으려면 ES6 스프레드 구문 (spread syntax) 을 `Math.min()` 및 `Date` 생성자와 함께 사용할 수 있습니다. 다음은 코드 예시입니다.

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

이 함수를 사용하려면 `Date` 객체의 배열을 생성하고 스프레드 구문을 사용하여 `minDate()`에 전달합니다. 다음은 예시입니다.

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // Returns a `Date` object representing 2016-01-08T22:00:00.000Z
```

이 코드를 사용하면 JavaScript 에서 최소 날짜 값을 쉽게 찾을 수 있습니다.
