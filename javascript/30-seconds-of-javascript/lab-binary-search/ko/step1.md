# 이진 탐색 알고리즘 (Binary Search Algorithm)

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 이진 탐색 알고리즘은 정렬된 배열에서 주어진 요소의 인덱스를 찾는 데 사용됩니다. 이진 탐색 알고리즘을 구현하는 단계는 다음과 같습니다.

1. 왼쪽 및 오른쪽 검색 경계인 `l`과 `r`을 선언하고, 각각 `0`과 배열의 `length`로 초기화합니다.
2. `while` 루프를 사용하여 `Math.floor()`를 사용하여 검색 하위 배열을 반으로 나누어 검색 범위를 반복적으로 좁힙니다.
3. 요소가 발견되면 해당 인덱스를 반환합니다. 그렇지 않으면 `-1`을 반환합니다.
4. 이 알고리즘은 배열에 중복된 값을 고려하지 않습니다.

다음은 JavaScript 에서 이진 탐색 알고리즘을 구현한 예입니다.

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

다음 예제를 사용하여 `binarySearch` 함수를 테스트할 수 있습니다.

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
