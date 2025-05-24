# 정렬된 배열에서 삽입 인덱스 찾기 함수

배열에 값을 삽입하고 정렬 순서를 유지하기 위한 가장 낮은 인덱스를 찾으려면 JavaScript 에서 `sortedIndexBy(arr, n, fn)` 함수를 사용하십시오.

이 함수는 배열이 내림차순으로 정렬되었는지 대략적으로 확인한 다음, 반복자 함수 `fn`을 기반으로 적절한 인덱스를 찾기 위해 `Array.prototype.findIndex()`를 사용합니다.

다음은 `sortedIndexBy()` 함수의 코드입니다.

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

객체 배열, 삽입할 값, 그리고 반복자 함수를 사용하여 함수를 호출할 수 있습니다.

예를 들어, `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)`는 `0`을 반환합니다. 이는 `x` 속성을 기준으로 정렬 순서를 유지하기 위해 `{ x: 4 }` 객체를 삽입해야 하는 인덱스입니다.
