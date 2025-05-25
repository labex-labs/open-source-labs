# 배열을 N 개의 청크로 분할하는 방법

배열을 `n`개의 더 작은 배열로 분할하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.ceil()`과 `Array.prototype.length`를 사용하여 각 청크의 크기를 계산합니다.
3. `Array.from()`을 사용하여 크기가 `n`인 새 배열을 생성합니다.
4. `Array.prototype.slice()`를 사용하여 새 배열의 각 요소를 `size` 길이의 청크에 매핑합니다.
5. 원래 배열을 균등하게 분할할 수 없는 경우, 마지막 청크에는 나머지 요소가 포함됩니다.

다음은 JavaScript 에서 `chunkIntoN` 함수의 예시 구현입니다.

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

이 함수를 사용하여 배열과 원하는 청크 수를 인수로 전달하여 배열을 `n`개의 청크로 분할할 수 있습니다. 예를 들어:

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
