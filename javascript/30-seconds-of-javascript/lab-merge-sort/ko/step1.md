# 병합 정렬 (Merge Sort) 알고리즘

병합 정렬 알고리즘을 사용하여 코딩을 연습하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. 재귀 (recursion) 를 사용하여 숫자 배열을 정렬합니다.
3. 배열의 `length`가 `2` 미만이면 배열을 반환합니다.
4. `Math.floor()`를 사용하여 배열의 중간 지점을 계산합니다.
5. `Array.prototype.slice()`를 사용하여 배열을 두 부분으로 나누고, 생성된 하위 배열에 대해 `mergeSort()`를 재귀적으로 호출합니다.
6. 마지막으로 `Array.from()`과 `Array.prototype.shift()`를 사용하여 정렬된 두 하위 배열을 하나로 결합합니다.

다음은 코드입니다.

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

다음 예시로 시도해 보세요.

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
