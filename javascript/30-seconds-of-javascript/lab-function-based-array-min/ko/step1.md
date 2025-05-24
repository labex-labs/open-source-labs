# 배열의 최소값을 반환하는 함수

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수는 제공된 함수를 기반으로 배열의 최소값을 반환합니다.

이를 위해 `Array.prototype.map()`을 사용하여 각 요소를 함수에서 반환된 값에 매핑합니다. 그런 다음 `Math.min()`을 사용하여 최소값을 구합니다.

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

이 함수는 배열과 함수를 전달하여 사용할 수 있습니다. 예를 들어:

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
