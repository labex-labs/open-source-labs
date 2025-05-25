# 퀵 정렬 알고리즘 (Quick Sort Algorithm)

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 알고리즘은 퀵 정렬 알고리즘을 사용하여 숫자 배열을 정렬합니다. 다음은 따라야 할 단계입니다.

- 재귀 (recursion) 를 사용합니다.
- 스프레드 연산자 (`...`) 를 사용하여 원본 배열 `arr`을 복제합니다.
- 배열의 `length`가 `2` 미만이면 복제된 배열을 반환합니다.
- `Math.floor()`를 사용하여 피벗 요소의 인덱스를 계산합니다.
- `Array.prototype.reduce()`와 `Array.prototype.push()`를 사용하여 배열을 두 개의 하위 배열로 분할합니다. 첫 번째 하위 배열은 `pivot`보다 작거나 같은 요소를 포함하고, 두 번째 하위 배열은 그보다 큰 요소를 포함합니다. 결과를 두 개의 배열로 분해합니다 (destructure).
- 생성된 하위 배열에 대해 `quickSort()`를 재귀적으로 호출합니다.

다음은 이 알고리즘을 구현하는 방법의 예입니다.

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

테스트하려면 다음 명령을 실행하십시오.

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
