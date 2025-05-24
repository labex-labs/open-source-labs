# JavaScript 에서 역순 범위로 배열을 초기화하는 방법

JavaScript 에서 역순 범위로 배열을 초기화하려면 다음 함수를 사용하십시오.

```js
const initializeArrayWithRangeRight = (end, start = 0, step = 1) =>
  Array.from({ length: Math.ceil((end + 1 - start) / step) }).map(
    (v, i, arr) => (arr.length - i - 1) * step + start
  );
```

이 함수는 지정된 범위의 숫자를 역순으로 포함하는 배열을 생성합니다. `start` 및 `end` 매개변수는 포함적이며, `step` 매개변수는 범위 내 숫자 간의 공차를 지정합니다.

함수를 사용하려면 다음과 같이 원하는 `end`, `start`, 및 `step` 값을 인수로 호출하십시오.

```js
initializeArrayWithRangeRight(5); // [5, 4, 3, 2, 1, 0]
initializeArrayWithRangeRight(7, 3); // [7, 6, 5, 4, 3]
initializeArrayWithRangeRight(9, 0, 2); // [8, 6, 4, 2, 0]
```

`start` 인수를 생략하면 기본값은 `0`입니다. `step` 인수를 생략하면 기본값은 `1`입니다.
