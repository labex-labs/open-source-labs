# 함수 기반 배열 요소 제거

배열에서 특정 요소를 제거하려면 `dropWhile` 함수를 사용합니다. 이 함수는 전달된 함수가 `true`를 반환할 때까지 요소를 제거합니다. 그런 다음 함수는 배열의 나머지 요소를 반환합니다.

작동 방식은 다음과 같습니다.

- `Array.prototype.slice()`를 사용하여 배열을 반복 처리하여 `func`에서 반환된 값이 `true`가 될 때까지 배열의 첫 번째 요소를 제거합니다.
- 나머지 요소를 반환합니다.

사용 예시:

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
