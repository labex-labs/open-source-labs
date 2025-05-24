# 배열 대칭 차이 (Symmetric Difference) 를 찾는 함수

제공된 함수를 비교자 (comparator) 로 사용하여 두 배열 간의 대칭 차이를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.filter()` 및 `Array.prototype.findIndex()` 메서드를 사용하여 적절한 값을 찾습니다.
3. 주어진 코드를 사용하여 작업을 수행합니다.

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

예를 들어, 다음 입력을 고려해 보세요.

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

위의 코드는 두 배열 간의 대칭 차이로 `[1, 1.2, 3.9]`를 반환합니다.
