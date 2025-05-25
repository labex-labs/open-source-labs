# JavaScript 에서 배열의 마지막 N 개 요소 가져오는 방법

JavaScript 에서 배열의 마지막 `n`개 요소를 가져오려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. `Array.prototype.slice()`를 시작 값 `-n`과 함께 사용하여 배열의 마지막 `n`개 요소를 가져옵니다.

다음은 배열의 마지막 `n`개 요소를 가져오는 JavaScript 코드입니다.

```js
const lastN = (arr, n) => arr.slice(-n);
```

코드를 테스트하려면 배열과 가져오려는 요소의 수를 사용하여 `lastN()` 함수를 호출합니다. 예시:

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
