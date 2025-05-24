# 함수를 사용하여 고유하지 않은 배열 값 필터링

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

이 코드는 제공된 비교자 함수를 기반으로 배열에서 고유하지 않은 값을 필터링합니다. 이를 달성하기 위한 단계는 다음과 같습니다.

1. `Array.prototype.filter()` 및 `Array.prototype.every()`를 사용하여 비교자 함수 `fn`을 기반으로 고유한 값만 포함하는 새로운 배열을 생성합니다.
2. 비교자 함수는 비교되는 두 요소의 값과 해당 인덱스, 총 4 개의 인수를 받습니다.
3. 함수 `filterNonUniqueBy`는 위의 단계를 구현하고 고유한 값 배열을 반환합니다.

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

이 함수를 사용하는 방법의 예는 다음과 같습니다.

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

이 코드는 간결하고 명확하며 일관성이 있으며 예상대로 작동해야 합니다.
