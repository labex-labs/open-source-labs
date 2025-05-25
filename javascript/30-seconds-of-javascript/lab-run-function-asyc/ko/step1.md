# Web Worker 를 사용한 비동기 함수 실행

UI 를 차단하지 않고 함수를 실행하려면 Web Worker 를 사용하여 별도의 스레드에서 함수를 실행하십시오. 방법은 다음과 같습니다.

1. 실행할 함수의 문자열화된 버전을 내용으로 하는 `Blob` 객체 URL 을 사용하여 `Worker`를 생성합니다.
2. 함수 호출의 반환 값을 즉시 게시합니다.
3. `onmessage` 및 `onerror` 이벤트를 수신하고, worker 에서 다시 게시된 데이터를 resolve 하거나 오류를 throw 하는 `Promise`를 반환합니다.

```js
const runAsync = (fn) => {
  const worker = new Worker(
    URL.createObjectURL(new Blob([`postMessage((${fn})());`]), {
      type: "application/javascript; charset=utf-8"
    })
  );
  return new Promise((resolve, reject) => {
    worker.onmessage = ({ data }) => {
      resolve(data);
      worker.terminate();
    };
    worker.onerror = (error) => {
      reject(error);
      worker.terminate();
    };
  });
};
```

`runAsync`에 제공된 함수는 모든 것이 문자열화되어 리터럴이 되므로 클로저 (closure) 를 사용해서는 안 됩니다. 따라서 모든 변수와 함수는 내부에서 정의되어야 합니다. 다음은 몇 가지 예입니다.

```js
const longRunningFunction = () => {
  let result = 0;
  for (let i = 0; i < 1000; i++)
    for (let j = 0; j < 700; j++)
      for (let k = 0; k < 300; k++) result = result + i + j + k;

  return result;
};

runAsync(longRunningFunction).then(console.log); // 209685000000
runAsync(() => 10 ** 3).then(console.log); // 1000
let outsideVariable = 50;
runAsync(() => typeof outsideVariable).then(console.log); // 'undefined'
```
