# 일련의 프로미스 실행

일련의 프로미스 배열을 실행하려면 `Array.prototype.reduce()`를 사용하여 프로미스 체인 (promise chain) 을 생성합니다. 각 프로미스는 해결된 후 다음 프로미스를 반환합니다.

시작하려면 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

다음은 코드의 예입니다.

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

그런 다음 `runPromisesInSeries` 함수를 사용하여 다음과 같이 프로미스를 순차적으로 실행할 수 있습니다.

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// This code runs each promise sequentially, taking a total of 3 seconds to complete.
```
