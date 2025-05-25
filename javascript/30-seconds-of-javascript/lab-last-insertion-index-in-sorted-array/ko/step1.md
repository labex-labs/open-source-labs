# 정렬된 배열에서 마지막 삽입 인덱스 설명

정렬 순서를 유지하기 위해 배열에 값을 삽입해야 하는 가장 높은 인덱스를 찾으려면 다음 단계를 따르세요.

- 먼저, 배열이 내림차순으로 정렬되었는지 대략적으로 확인합니다.
- 그런 다음, `Array.prototype.reverse()` 및 `Array.prototype.findIndex()`를 사용하여 요소가 삽입되어야 하는 적절한 마지막 인덱스를 찾습니다.

다음은 해당 함수에 대한 코드입니다.

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

다음은 이 함수를 사용하는 예시입니다.

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.
