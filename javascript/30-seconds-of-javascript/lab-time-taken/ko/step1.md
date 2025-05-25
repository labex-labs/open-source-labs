# 함수 실행 시간 측정

함수 실행 시간을 측정하려면 `console.time()`과 `console.timeEnd()`를 사용하여 시작 시간과 종료 시간의 차이를 결정합니다.

다음은 콜백 함수 실행 시간을 측정하는 `timeTaken`이라는 예시 함수입니다.

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

이 함수를 사용하려면 콜백을 인수로 전달하기만 하면 됩니다. 예를 들어:

```js
timeTaken(() => Math.pow(2, 10)); // Returns 1024, and logs: timeTaken: 0.02099609375ms
```

위의 예에서 `timeTaken` 함수는 `Math.pow(2, 10)` 함수 호출을 실행하는 데 걸린 시간을 측정하는 데 사용되며, 1024 를 반환합니다. 콘솔 출력은 밀리초 (ms) 단위로 소요 시간을 표시합니다.
