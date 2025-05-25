# Promisify 함수

비동기 함수가 프로미스 (Promise) 를 반환하도록 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 커링 (currying) 을 사용하여 원래 함수를 호출하는 `Promise`를 반환하는 함수를 반환합니다.
3. 나머지 연산자 (`...`) 를 사용하여 모든 매개변수를 전달합니다.
4. Node 8+ 를 사용하는 경우 [`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original)를 사용할 수 있습니다.
5. 다음은 코드 예시입니다.

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6. 이 함수를 사용하려면 비동기 함수를 정의하고 `promisify` 함수에 매개변수로 전달합니다. 이제 반환된 함수는 프로미스를 반환합니다.

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // Promise resolves after 2s
```

`delay` 함수는 `promisify` 함수를 사용하여 이제 프로미스를 반환하는 비동기 함수의 예입니다.
