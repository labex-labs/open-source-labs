# 조건이 충족될 때까지 배열 끝에서 요소 제거하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 전달된 함수가 `false`를 반환할 때까지 배열의 끝에서 요소를 제거하는 함수입니다. 그런 다음 제거된 요소를 반환합니다.

이 함수를 사용하려면 스프레드 연산자 (`...`) 와 `Array.prototype.reverse()`를 사용하여 배열의 역본을 만듭니다. 그런 다음, 함수의 반환 값이 falsy 가 될 때까지 `Array.prototype.entries()`에 대한 `for...of` 루프를 사용하여 역본을 반복합니다.

콜백 함수 `fn`은 요소의 값인 단일 인수를 받습니다. 마지막으로 `Array.prototype.slice()`를 사용하여 제거된 요소를 반환합니다.

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

다음은 이 함수를 사용하는 예시입니다.

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
