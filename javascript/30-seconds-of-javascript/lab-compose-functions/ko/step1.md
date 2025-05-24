# JavaScript 에서 함수를 합성하는 방법

JavaScript 에서 함수 합성을 사용하여 코딩을 연습하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

다음은 JavaScript 에서 오른쪽에서 왼쪽으로 함수 합성을 수행하는 방법의 예입니다.

1. `Array.prototype.reduce()`를 사용하여 오른쪽에서 왼쪽으로 함수 합성을 수행합니다.
2. 마지막 (가장 오른쪽에 있는) 함수는 하나 이상의 인수를 허용할 수 있으며, 나머지 함수는 단항 (unary) 이어야 합니다.
3. 임의의 수의 함수를 인수로 받아 이를 합성하는 새로운 함수를 반환하는 `compose` 함수를 정의합니다.
4. 원하는 순서로 원하는 함수를 사용하여 `compose` 함수를 호출합니다.
5. 필요한 인수를 사용하여 새로 합성된 함수를 호출합니다.

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

예를 들어, 두 개의 함수가 있다고 가정해 보겠습니다.

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

`compose`를 사용하여 이러한 함수를 합성할 수 있습니다.

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

이제 원하는 인수를 사용하여 `multiplyAndAdd5`를 호출할 수 있습니다.

```js
multiplyAndAdd5(5, 2); // 15
```
