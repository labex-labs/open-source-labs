# 수렴 함수 (Converging Functions)

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수 `converge`는 수렴 함수 (converging function) 와 분기 함수 (branching functions) 목록을 입력으로 받습니다. 이 함수는 각 분기 함수를 입력 인수에 적용하는 새로운 함수를 반환합니다. 그런 다음 분기 함수의 결과는 수렴 함수에 인수로 전달됩니다.

`Array.prototype.map()` 및 `Function.prototype.apply()` 메서드는 각 함수를 입력 인수에 적용하는 데 사용됩니다. 스프레드 연산자 (`...`) 는 다른 모든 함수의 결과를 사용하여 `converger`를 호출하는 데 사용됩니다.

다음은 `converge` 함수의 코드입니다.

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

이 함수를 사용하는 방법의 예는 아래에 나와 있습니다. `average` 함수는 배열의 평균을 계산하는 익명 함수로 `converge`를 호출하여 생성됩니다. 분기 함수는 각각 배열의 합계와 길이를 계산하는 두 개의 익명 함수입니다.

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

이 코드는 배열 `[1, 2, 3, 4, 5, 6, 7]`의 평균을 계산하고 `4`를 반환합니다.
