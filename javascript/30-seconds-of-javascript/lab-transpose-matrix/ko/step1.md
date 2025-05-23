# JavaScript 에서 행렬 전치하기

JavaScript 에서 2 차원 배열을 전치하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()`을 사용하여 주어진 2 차원 배열의 전치 행렬을 만듭니다. `map()` 메서드는 배열의 각 요소에 제공된 함수를 호출한 결과로 새 배열을 생성합니다.
3. 제공된 함수는 두 개의 인수를 받습니다: 배열의 현재 요소와 해당 인덱스입니다. 이 경우, 전치 행렬을 만들기 위해 인덱스만 필요합니다.
4. 인덱스를 사용하여 2 차원 배열의 각 행에서 해당 요소에 접근하고 해당 요소로 새 배열을 만듭니다. 이것이 전치된 배열의 새 행이 됩니다.
5. 2 차원 배열의 각 열에 대해 이전 단계를 반복하여 완전한 전치 배열을 만듭니다.

다음은 JavaScript 에서 2 차원 배열을 전치하는 코드입니다.

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
