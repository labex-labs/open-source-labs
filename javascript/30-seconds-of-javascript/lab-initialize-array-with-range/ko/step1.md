# 범위로 배열 초기화 함수

숫자 범위로 배열을 초기화하려면 다음 함수를 사용하십시오.

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

이 함수는 세 개의 인수를 받습니다: `end` (필수), `start` (선택 사항, 기본값은 `0`), 그리고 `step` (선택 사항, 기본값은 `1`). 이 함수는 지정된 범위 내의 숫자를 포함하는 배열을 반환하며, 여기서 `start`와 `end`는 공차 `step`을 포함합니다.

이 함수를 사용하려면 원하는 범위 매개변수로 호출하기만 하면 됩니다.

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

이 함수는 `Array.from()`을 사용하여 원하는 길이의 배열을 생성한 다음, map 함수를 사용하여 주어진 범위 내에서 원하는 값으로 배열을 채웁니다. 두 번째 인수 `start`를 생략하면 기본값 `0`을 사용합니다. 마지막 인수 `step`을 생략하면 기본값 `1`을 사용합니다.
