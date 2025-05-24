# 함수 기반 고유 배열 값 필터링

다음은 비교 함수 (`fn`) 를 기반으로 고유한 값을 필터링하여 고유하지 않은 값만 포함하는 배열을 생성하는 방법입니다.

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

이 함수를 사용하려면 필터링하려는 배열과 비교 함수 (comparator function) 의 두 인수를 사용하여 `filterUniqueBy()`를 호출합니다. 비교 함수는 두 개의 비교되는 요소의 값과 해당 인덱스, 총 4 개의 인수를 가져야 합니다.

예를 들어, 객체 배열이 있고 고유한 `id` 값을 가진 객체를 필터링하려는 경우 다음과 같이 할 수 있습니다.

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
