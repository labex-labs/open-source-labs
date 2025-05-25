# 매핑된 배열 요소의 합계를 계산하는 함수

제공된 함수를 사용하여 각 요소를 값에 매핑하여 배열의 합계를 계산하려면 `sumBy` 함수를 사용하십시오. 이 함수는 `Array.prototype.map()`을 사용하여 각 요소를 `fn`에서 반환된 값에 매핑합니다. 그런 다음 `Array.prototype.reduce()`를 사용하여 각 값을 누산기에 더하며, 누산기는 `0` 값으로 초기화됩니다.

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

사용 예시:

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // Returns 20
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // Returns 20
```

이 함수로 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
