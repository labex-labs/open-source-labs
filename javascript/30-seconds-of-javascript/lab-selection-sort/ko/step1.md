# 선택 정렬 알고리즘

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음 함수는 선택 정렬 알고리즘을 사용하여 숫자 배열을 정렬합니다.

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

함수를 사용하려면 다음과 같이 `selectionSort()`에 숫자 배열을 전달합니다.

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

이 함수는 spread operator (`...`) 를 사용하여 원래 배열을 복제하여 작동합니다. 그런 다음 `for` 루프를 사용하여 배열을 반복합니다. `Array.prototype.slice()` 및 `Array.prototype.reduce()`를 사용하여 현재 인덱스 오른쪽에 있는 하위 배열에서 최소 요소의 인덱스를 찾습니다. 필요한 경우 swap 을 수행합니다.
