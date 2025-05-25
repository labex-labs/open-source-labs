# 조건에 따라 배열 요소 제거하기

조건에 따라 배열의 요소를 제거하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`takeWhile` 함수는 전달된 함수가 `false`를 반환할 때까지 배열에서 요소를 제거한 다음 제거된 요소를 반환합니다.

`takeWhile` 함수를 사용하는 단계는 다음과 같습니다.

- `Array.prototype.entries()`를 사용하여 `for...of` 루프를 통해 배열을 반복합니다.
- 함수에서 반환된 값이 falsy 가 될 때까지 반복합니다.
- `Array.prototype.slice()`를 사용하여 제거된 요소를 반환합니다.
- `fn` 콜백 함수는 요소의 값인 단일 인수를 받습니다.

`takeWhile` 함수를 구현하려면 다음 코드를 사용하십시오.

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

다음은 `takeWhile` 함수를 사용하여 조건에 따라 배열에서 요소를 제거하는 예입니다.

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
