# JavaScript 에서 함수의 이름 얻는 방법

JavaScript 함수의 이름을 얻으려면 다음 단계를 따르세요.

1. 터미널 또는 SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. `console.debug()`와 전달된 함수의 `name` 속성을 사용하여 함수의 이름을 콘솔의 `debug` 채널에 로깅합니다.
4. 주어진 함수 `fn`을 반환합니다.

다음은 JavaScript 에서 함수의 이름을 얻는 방법을 보여주는 코드 예시입니다.

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// The function name 'max' is logged in the debug channel of the console.
// m = 6
```

이 예제에서 `functionName` 함수는 전달된 함수의 이름을 콘솔의 `debug` 채널에 로깅하고 함수 자체를 반환합니다. 함수의 `name` 속성은 해당 이름을 얻는 데 사용됩니다.
