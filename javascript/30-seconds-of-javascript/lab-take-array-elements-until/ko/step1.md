# 조건이 충족될 때까지 배열 요소 제거하기

조건이 충족될 때까지 배열의 요소를 제거하고 제거된 요소를 얻으려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- 인수로 전달된 함수가 truthy 값을 반환할 때까지 `Array.prototype.entries()`를 사용하여 `for...of` 루프를 통해 배열을 반복합니다.
- `Array.prototype.slice()`를 사용하여 제거된 요소를 반환합니다.
- 콜백 함수 `fn`은 요소의 값인 단일 인수를 받습니다.

다음은 코드 스니펫 예시입니다.

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

위의 예제에서 `takeUntil()` 함수는 값이 3 이상이 될 때까지 `[1, 2, 3, 4]` 배열의 요소를 제거하는 데 사용됩니다. 출력은 `[1, 2]`입니다.
