# 연속된 요소의 배열 찾기

연속된 요소의 배열을 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.slice()`를 사용하여 시작 부분에서 `n - 1`개의 요소가 제거된 배열을 생성합니다.
3. `Array.prototype.map()` 및 `Array.prototype.slice()`를 사용하여 각 요소를 `n`개의 연속된 요소의 배열에 매핑합니다.

다음은 이러한 단계를 구현하는 예시 함수입니다.

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

이 함수를 배열과 숫자 `n`과 함께 호출하여 배열에서 `n`개의 연속된 모든 요소의 배열을 찾을 수 있습니다. 예를 들어:

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
