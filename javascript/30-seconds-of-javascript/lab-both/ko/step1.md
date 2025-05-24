# 함수와 논리 AND 사용하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

두 함수가 주어진 인수에 대해 `true`를 반환하는지 확인하려면 논리 AND (`&&`) 연산자를 사용합니다.

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

위 코드는 두 개의 함수 `f`와 `g`를 입력으로 받아들이고, 제공된 인수로 `f`와 `g`를 호출하여 두 함수 모두 `true`를 반환하는 경우에만 `true`를 반환하는 다른 함수를 반환하는 새로운 함수 `both`를 생성합니다.

예를 들어, 숫자가 양수이면서 짝수인지 확인하려면 아래와 같이 `isEven` 및 `isPositive` 함수를 `both`와 함께 사용할 수 있습니다.

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

여기서 `isPositiveEven`은 `isEven`과 `isPositive`를 입력으로 사용하여 `both` 함수를 통해 주어진 숫자가 양수이면서 짝수인지 확인하는 새로운 함수입니다.
