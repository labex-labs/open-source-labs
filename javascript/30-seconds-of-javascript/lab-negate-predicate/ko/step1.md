# JavaScript 에서 술어 함수를 부정하는 방법

JavaScript 에서 술어 함수를 부정하려면 `!` 연산자를 사용할 수 있습니다. 이를 위해 술어 함수를 인수로 받아 해당 인수에 `!` 연산자를 적용하는 `negate`라는 고차 함수를 만들 수 있습니다. 다음은 `negate`를 구현하는 예시입니다.

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

그런 다음 `negate`를 사용하여 모든 술어 함수를 부정할 수 있습니다. 다음은 `negate`를 사용하여 배열에서 짝수를 필터링하는 예시입니다.

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

이 예제에서 `isEven`은 숫자가 짝수인지 확인하는 술어 함수입니다. 그런 다음 `negate`를 사용하여 `isEven`을 부정함으로써 숫자가 홀수인지 확인하는 `isOdd`라는 새로운 술어 함수를 만듭니다. 마지막으로 `isOdd`를 `filter` 메서드와 함께 사용하여 배열에서 짝수를 필터링합니다.
