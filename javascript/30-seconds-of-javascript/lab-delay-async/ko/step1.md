# JavaScript 에서 비동기 함수 실행을 지연시키는 방법

JavaScript 에서 비동기 함수 실행을 지연시키려면 아래의 `sleep` 함수를 사용할 수 있습니다. 이 함수는 특정 시간 후에 해결되는 `Promise`를 반환합니다. `sleep`을 사용하여 `async` 함수의 일부 실행을 지연시키는 방법의 예는 다음과 같습니다.

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("I'm going to sleep for 1 second.");
  await sleep(1000);
  console.log("I woke up after 1 second.");
}
```

이 함수를 사용하려면 `sleepyWork()`를 호출하기만 하면 됩니다. 그러면 콘솔에 메시지가 1 초 간격으로 로깅됩니다.
