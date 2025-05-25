# 안정 정렬 (Stable Sort)

배열의 안정 정렬을 수행하고 동일한 값을 가진 항목의 초기 인덱스를 유지하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()`을 사용하여 입력 배열의 각 요소를 해당 인덱스와 쌍으로 묶습니다.
3. `Array.prototype.sort()`를 `compare` 함수와 함께 사용하여 비교되는 항목이 같을 경우 초기 순서를 유지하면서 목록을 정렬합니다.
4. `Array.prototype.map()`을 다시 사용하여 배열 항목을 초기 형태로 변환합니다.
5. 원본 배열은 변경되지 않고 새로운 배열이 대신 반환됩니다.

다음은 JavaScript 에서 `stableSort` 함수의 구현입니다.

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

아래와 같이 배열과 `compare` 함수를 사용하여 `stableSort` 함수를 호출하여 정렬된 항목이 있는 새 배열을 얻을 수 있습니다.

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
