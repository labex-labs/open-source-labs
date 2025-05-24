# JavaScript 에서 재귀를 사용하여 배열을 깊이 평탄화하는 방법

JavaScript 에서 배열을 깊이 평탄화하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀를 사용하여 배열을 평탄화합니다.
3. 빈 배열 (`[]`) 과 스프레드 연산자 (`...`) 를 사용하여 `Array.prototype.concat()` 메서드를 사용해 배열을 평탄화합니다.
4. 배열인 각 요소를 재귀적으로 평탄화합니다.
5. 다음 코드를 구현합니다.

```js
const deepFlatten = (arr) =>
  [].concat(...arr.map((v) => (Array.isArray(v) ? deepFlatten(v) : v)));

deepFlatten([1, [2], [[3], 4], 5]); // [1, 2, 3, 4, 5]
```

이러한 단계를 따르면 JavaScript 에서 재귀를 사용하여 배열을 쉽게 깊이 평탄화할 수 있습니다.
