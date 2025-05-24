# JavaScript 에서 배열 교차 곱 생성하기

JavaScript 에서 배열 교차 곱을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`, `Array.prototype.map()`, 그리고 `Array.prototype.concat()`을 사용하여 두 배열의 요소에서 가능한 모든 쌍을 생성합니다.
3. 함수 `xProd()`는 두 개의 배열을 인수로 받아 배열에서 가능한 각 쌍을 생성하여 제공된 두 배열에서 새로운 배열을 만듭니다.
4. 다음은 `xProd()` 함수의 작동 예시입니다.

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

이것은 두 입력 배열의 모든 가능한 요소 쌍을 포함하는 배열을 반환합니다.
