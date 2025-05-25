# JavaScript 에서 비동기 함수 파이핑 (Piping) 방법

JavaScript 로 코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 기본 사항에 익숙해지면 비동기 함수로 작업할 수 있습니다.

`pipeAsyncFunctions` 함수를 사용하면 비동기 함수를 사용하여 왼쪽에서 오른쪽으로 함수 합성을 수행할 수 있습니다. 작동 방식은 다음과 같습니다.

- 이 함수는 임의의 수의 비동기 함수를 인수로 받습니다.
- 스프레드 연산자 (`...`) 는 이러한 함수를 `pipeAsyncFunctions` 함수에 개별 인수로 전달하는 데 사용됩니다.
- 결과 함수는 임의의 수의 인수를 허용할 수 있지만, 합성되는 각 함수는 단일 인수를 허용해야 합니다.
- 함수는 일반 값, Promise 의 조합을 반환하거나 `async`일 수 있으며 `await`를 통해 반환할 수 있습니다.
- `reduce()` 메서드는 `Promise.prototype.then()`과 함께 사용하여 함수 합성을 수행합니다.
- `reduce()` 메서드는 함수를 반복하여 각 함수를 순차적으로 실행하고 한 함수의 결과를 다음 함수에 전달합니다.
- 결과 Promise 가 반환됩니다.

다음은 `pipeAsyncFunctions`를 사용하여 숫자를 더하는 방법의 예입니다.

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4
);
(async () => {
  console.log(await sum(5)); // 15 (after one second)
})();
```

이 예에서 `sum`은 입력 숫자에 서로 다른 값을 더하는 네 개의 함수로 구성됩니다. `sum`의 최종 값은 각 함수를 순차적으로 실행한 결과이며, 두 번째 함수에 대해 1 초의 지연이 있습니다. `async` 키워드는 `await`를 사용할 수 있도록 마지막 함수와 함께 사용됩니다.

`pipeAsyncFunctions`를 사용하면 임의의 수의 비동기 함수를 쉽게 함께 합성하여 더 복잡한 기능을 만들 수 있습니다.
