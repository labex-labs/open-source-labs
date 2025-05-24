# 함수 기반으로 배열 요소 오른쪽에서 제거하기

특정 조건이 충족될 때까지 배열의 끝에서 요소를 제거하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.slice()`를 사용하여 배열을 반복하고 전달된 `func`가 `true`를 반환할 때까지 배열의 마지막 요소를 제거합니다.
3. 배열에 남아있는 요소를 반환합니다.

다음은 예시 구현입니다.

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

이 함수는 다음과 같이 사용할 수 있습니다.

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
