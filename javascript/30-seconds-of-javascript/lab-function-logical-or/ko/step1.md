# 함수에 논리 OR 사용하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

논리 OR (`||`) 연산자는 주어진 인수에 대해 적어도 하나의 함수가 `true`를 반환하는지 확인하는 데 사용할 수 있습니다. 이를 위해 제공된 `args`로 두 함수를 호출하고 결과에 논리 OR 연산자를 적용합니다.

다음은 `either` 함수의 예시 구현입니다.

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

다음은 두 함수 `isEven`과 `isPositive`를 사용하여 `either` 함수를 사용하는 예시입니다.

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

이 예제에서 `isPositiveOrEven`은 `4`와 `3` 모두에 대해 `true`를 반환합니다. 왜냐하면 `isEven`은 `4`에 대해 `true`를 반환하고 `isPositive`는 `3`에 대해 `true`를 반환하기 때문입니다.
