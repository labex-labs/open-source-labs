# 피보나치 수열

JavaScript 에서 피보나치 수열을 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. `Array.from()`을 사용하여 특정 길이의 빈 배열을 생성하고 처음 두 값 (`0`과 `1`) 을 초기화합니다.
3. `Array.prototype.reduce()`와 `Array.prototype.concat()`을 사용하여 배열에 값을 추가합니다. 처음 두 값을 제외하고 마지막 두 값의 합을 사용합니다.
4. `fibonacci()` 함수를 호출하고 원하는 수열의 길이를 인수로 전달합니다.

다음은 코드입니다.

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

이렇게 하면 n 번째 항까지의 피보나치 수열을 포함하는 배열이 생성됩니다.
