# JavaScript 에서 N 차원 배열 초기화 방법

JavaScript 에서 N 차원 배열을 생성하려면 `initializeNDArray` 함수를 사용할 수 있습니다. 이 함수는 값과 임의의 차원 수를 인수로 받아 해당 값으로 초기화된 새 배열을 반환합니다.

`initializeNDArray`를 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. 재귀를 사용하여 주어진 차원 수로 배열을 생성합니다.
3. `Array.from()` 및 `Array.prototype.map()`을 사용하여 각 행이 `initializeNDArray()`를 사용하여 초기화된 새 배열인 행을 생성합니다.

다음은 `initializeNDArray` 함수의 코드입니다.

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

그런 다음 원하는 값과 차원 수로 `initializeNDArray`를 호출할 수 있습니다. 예를 들어:

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
