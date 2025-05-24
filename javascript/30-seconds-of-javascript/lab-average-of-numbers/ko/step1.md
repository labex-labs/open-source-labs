# JavaScript 에서 숫자 평균 계산 방법

JavaScript 에서 두 개 이상의 숫자의 평균을 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 내장된 `Array.prototype.reduce()` 메서드를 사용하여 각 값을 `0`으로 초기화된 누산기 (accumulator) 에 더합니다.
3. 결과 합계를 배열의 길이로 나눕니다.

다음은 사용할 수 있는 예시 코드 조각입니다.

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

`average` 함수는 배열 또는 여러 인수를 사용하여 호출할 수 있습니다.

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
