# 값이 배열 유사 객체인지 확인하기

값이 배열 유사 객체인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력합니다.
3. 제공된 인수가 반복 가능한지 확인하려면 다음 코드를 사용합니다.

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. 함수는 제공된 인수가 배열 유사 객체인 경우 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.
5. 예를 들어:

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
