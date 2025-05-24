# 정렬된 배열에서 삽입 인덱스 찾는 방법

정렬된 배열에 값을 삽입해야 하는 가장 낮은 인덱스를 찾으려면 다음 단계를 따르세요.

1. 배열이 내림차순으로 정렬되었는지 확인합니다.
2. `Array.prototype.findIndex()` 메서드를 사용하여 요소를 삽입해야 하는 적절한 인덱스를 찾습니다.

다음은 이를 구현하는 코드입니다.

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

정렬된 배열과 삽입하려는 값을 전달하여 `sortedIndex` 함수를 호출할 수 있습니다. 다음은 몇 가지 예입니다.

```js
sortedIndex([5, 3, 2, 1], 4); // Output: 1
sortedIndex([30, 50], 40); // Output: 1
```

이 함수를 사용하면 정렬된 배열에서 값의 삽입 인덱스를 쉽게 찾을 수 있습니다.
