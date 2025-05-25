# 에라토스테네스의 체를 사용하여 소수 생성하기

에라토스테네스의 체를 사용하여 주어진 숫자까지의 소수를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `2`부터 주어진 숫자까지의 숫자를 포함하는 배열을 생성합니다.
3. `Array.prototype.filter()`를 사용하여 `2`부터 제공된 숫자의 제곱근까지의 숫자로 나누어 떨어지는 값을 필터링합니다.
4. 소수를 포함하는 결과 배열을 반환합니다.

다음은 주어진 숫자까지의 소수를 생성하는 JavaScript 코드입니다.

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

원하는 숫자를 인수로 전달하여 `generatePrimes()` 함수를 호출할 수 있습니다. 예를 들어:

```js
generatePrimes(10); // [2, 3, 5, 7]
```
