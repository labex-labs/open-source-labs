# 파이프를 사용한 함수 합성

파이프를 사용하여 코딩을 연습하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`pipeFunctions` 함수는 스프레드 연산자 (`...`) 와 함께 `Array.prototype.reduce()`를 사용하여 왼쪽에서 오른쪽으로 함수 합성을 수행합니다. 첫 번째 (가장 왼쪽) 함수는 하나 이상의 인수를 허용할 수 있지만, 나머지 함수는 단항 (unary) 이어야 합니다.

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

다음은 `pipeFunctions`를 사용하여 두 숫자를 곱한 다음 결과에 5 를 더하는 새로운 함수 `multiplyAndAdd5`를 만드는 예입니다.

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

이 예에서 `multiplyAndAdd5`는 두 개의 인수 `5`와 `2`를 받아 먼저 `multiply`를 적용하여 `10`을 생성한 다음, 결과에 `add5`를 적용하여 `15`를 생성하는 새로운 함수입니다.
