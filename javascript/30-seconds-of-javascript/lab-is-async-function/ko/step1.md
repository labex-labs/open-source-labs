# JavaScript 에서 값이 비동기 함수인지 확인하기

JavaScript 에서 값이 `async` 함수인지 확인하려면 다음 코드를 사용할 수 있습니다.

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

이 함수는 `Object.prototype.toString()` 및 `Function.prototype.call()`을 사용하여 주어진 인수가 `async` 함수인지 확인합니다.

일반 함수와 `async` 함수를 인수로 전달하여 함수를 테스트할 수 있습니다.

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

JavaScript 코딩을 연습하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
