# 힙 정렬 (Heap Sort) 알고리즘

코딩 연습을 위해 터미널/SSH 를 열고 'node'를 입력하세요. 다음 알고리즘은 힙 정렬 알고리즘을 사용하여 숫자 배열을 정렬합니다. 다음 단계를 따르세요:

- 함수에서 재귀 (recursion) 를 사용합니다.
- 스프레드 연산자 `(...)`를 사용하여 원래 배열 `arr`을 복제합니다.
- 클로저 (closures) 를 사용하여 변수 `l`과 함수 `heapify`를 선언합니다.
- `for` 루프와 `Math.floor()`를 `heapify`와 함께 사용하여 배열에서 최대 힙 (max heap) 을 생성합니다.
- `for` 루프를 사용하여 고려 범위를 반복적으로 좁히고, `heapify`를 사용하고 필요에 따라 값을 교환하여 복제된 배열을 정렬합니다.

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

예를 들어:

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
