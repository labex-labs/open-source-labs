# 버블 정렬 알고리즘

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하여 시작합니다. 버블 정렬 알고리즘은 숫자 배열을 정렬합니다.

버블 정렬 알고리즘을 사용하여 배열을 정렬하는 단계:

1. 현재 반복에서 값이 교환되었는지 여부를 나타내는 변수 `swapped`를 선언합니다.

2. 스프레드 연산자 (`...`) 를 사용하여 원래 배열 `arr`을 복제합니다.

3. `for` 루프를 사용하여 복제된 배열의 요소를 반복하고, 마지막 요소 전에 종료합니다.

4. 중첩된 `for` 루프를 사용하여 `0`과 `i` 사이의 배열 세그먼트를 반복하고, 순서가 잘못된 인접 요소를 교환하고 `swapped`를 `true`로 설정합니다.

5. 반복 후 `swapped`가 `false`이면 더 이상 변경이 필요 없으므로 복제된 배열이 반환됩니다.

예제 코드:

```js
const bubbleSort = (arr) => {
  let swapped = false;
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    swapped = false;
    for (let j = 0; j < a.length - i; j++) {
      if (a[j + 1] < a[j]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
      }
    }
    if (!swapped) return a;
  }
  return a;
};

bubbleSort([2, 1, 4, 3]); // [1, 2, 3, 4]
```
