# n 번째 인수를 가져오는 함수

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요. 인덱스 `n`에 있는 인수를 가져오는 함수를 만드는 방법은 다음과 같습니다.

- `Array.prototype.slice()`를 사용하여 인덱스 `n`에 있는 원하는 인수를 가져옵니다.
- `n`이 음수이면, 뒤에서 n 번째 인수가 반환됩니다.

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

`nthArg` 함수를 사용하는 예는 다음과 같습니다.

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // Output: 3
console.log(third(1, 2)); // Output: undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // Output: 5
```
