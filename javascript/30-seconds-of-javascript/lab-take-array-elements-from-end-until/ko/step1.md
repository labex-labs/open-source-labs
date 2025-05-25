# 조건이 충족될 때까지 배열 요소 끝에서 제거하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수는 전달된 함수가 `true`를 반환할 때까지 배열의 끝에서 요소를 제거한 다음 제거된 요소를 반환합니다.

작동 방식은 다음과 같습니다.

- 먼저, spread operator (`...`) 와 `Array.prototype.reverse()`를 사용하여 배열의 복사본을 반전시킵니다.
- 다음으로, `Array.prototype.entries()`에 대한 `for...of` 루프를 사용하여 함수에서 반환된 값이 truthy 가 될 때까지 반전된 복사본을 반복합니다.
- 그 후, `Array.prototype.slice()`를 사용하여 제거된 요소를 반환합니다.
- 콜백 함수 `fn`은 요소의 값인 단일 인수를 받습니다.

다음은 코드입니다.

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

다음은 이 함수를 사용하는 예입니다.

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
