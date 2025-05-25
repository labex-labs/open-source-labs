# 배열의 N 번째 요소 찾기

배열의 n 번째 요소를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.slice()`를 사용하여 n 번째 요소를 포함하는 새로운 배열을 생성합니다.
3. 인덱스가 범위를 벗어난 경우 `undefined`를 반환합니다.
4. 두 번째 인수 `n`을 생략하여 배열의 첫 번째 요소를 가져옵니다.

다음은 이를 구현하는 예제 코드입니다.

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

다음 예제를 사용하여 이 함수를 테스트할 수 있습니다.

```js
nthElement(["a", "b", "c"], 1); // Output: 'b'
nthElement(["a", "b", "b"], -3); // Output: 'a'
```

이러한 단계를 따르면 JavaScript 를 사용하여 배열의 n 번째 요소를 쉽게 찾을 수 있습니다.
