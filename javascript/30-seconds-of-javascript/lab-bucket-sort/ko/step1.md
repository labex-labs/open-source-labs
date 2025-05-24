# 버킷 정렬 알고리즘

버킷 정렬 알고리즘을 사용하여 숫자 배열을 정렬하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Math.min()`, `Math.max()` 및 스프레드 연산자 (`...`) 를 사용하여 주어진 배열의 최소값과 최대값을 찾습니다.
3. `Array.from()` 및 `Math.floor()`를 사용하여 적절한 수의 `buckets`(빈 배열) 를 생성합니다.
4. `Array.prototype.forEach()`를 사용하여 배열에서 각 버킷을 적절한 요소로 채웁니다.
5. `Array.prototype.reduce()`, 스프레드 연산자 (`...`) 및 `Array.prototype.sort()`를 사용하여 각 버킷을 정렬하고 결과에 추가합니다.

다음은 JavaScript 에서 버킷 정렬 알고리즘의 예시 구현입니다.

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => []
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

알고리즘을 테스트하려면 다음 코드를 실행하세요.

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
