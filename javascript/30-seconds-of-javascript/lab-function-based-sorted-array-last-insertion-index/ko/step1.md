# 함수 기반으로 정렬된 배열에서 마지막 삽입 인덱스를 찾는 방법

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

제공된 이터레이터 함수를 기반으로 배열의 정렬 순서를 유지하기 위해 값을 삽입해야 하는 가장 높은 인덱스를 찾는 방법은 다음과 같습니다.

1. 배열이 내림차순으로 정렬되었는지 확인합니다.
2. `Array.prototype.map()`을 사용하여 이터레이터 함수를 배열의 모든 요소에 적용합니다.
3. `Array.prototype.reverse()` 및 `Array.prototype.findIndex()`를 사용하여 제공된 이터레이터 함수를 기반으로 요소가 삽입되어야 하는 적절한 마지막 인덱스를 찾습니다.

아래 코드를 참조하세요:

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

다음은 예시입니다:

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
