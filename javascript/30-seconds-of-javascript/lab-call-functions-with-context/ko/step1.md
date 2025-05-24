# JavaScript 에서 컨텍스트와 함께 함수를 호출하는 방법

Node.js 에서 코드를 실행하려면 터미널/SSH 를 열고 `node`를 입력하십시오. JavaScript 에서 특정 컨텍스트와 일련의 인수를 사용하여 함수를 호출하려면 클로저 (closure) 를 사용할 수 있습니다. 방법은 다음과 같습니다.

1. `key`와 일련의 `args`를 매개변수로 받고 `context` 매개변수를 받는 새로운 함수를 반환하는 `call` 함수를 정의합니다.

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. `call` 함수를 사용하여 숫자 배열에 대해 `map` 함수를 호출합니다. 이 예제에서 `map` 함수는 배열의 각 숫자를 두 배로 만듭니다.

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. `call` 함수를 `map`과 같은 특정 키에 바인딩 (bind) 하여 숫자 배열에 대해 `map` 함수를 호출하는 데 사용할 수도 있습니다.

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

`call` 함수를 사용하면 특정 컨텍스트와 일련의 인수를 사용하여 모든 함수를 쉽게 호출할 수 있습니다.
