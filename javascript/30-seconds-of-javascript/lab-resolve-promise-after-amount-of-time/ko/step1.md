# 지연을 포함하는 Promise 생성

특정 시간 후에 resolve 되는 새로운 promise 를 생성하려면 다음 단계를 따르세요.

1. `Promise` 생성자를 사용하여 새로운 promise 를 생성합니다.
2. promise 의 실행자 함수 내부에서 `setTimeout()`을 사용하여 지정된 `delay` 후에 제공된 `value`로 promise 의 `resolve` 함수를 호출합니다.

다음은 `resolveAfter()`의 예시 구현입니다.

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

이제 `resolveAfter()`를 호출하여 지정된 지연 시간 후에 제공된 값으로 resolve 되는 promise 를 얻을 수 있습니다.

```js
resolveAfter("Hello", 1000);
// Returns a promise that resolves to 'Hello' after 1s
```

코딩 연습을 시작하려면 터미널 또는 SSH 를 열고 `node`를 입력하세요.
