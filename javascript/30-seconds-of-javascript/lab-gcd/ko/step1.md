# 최대 공약수 계산 방법

코드를 사용하여 두 개 이상의 숫자/배열 간의 최대 공약수 (GCD) 를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. 다음 코드를 사용합니다.

```js
const gcd = (...arr) => {
  const _gcd = (x, y) => (!y ? x : gcd(y, x % y));
  return [...arr].reduce((a, b) => _gcd(a, b));
};
```

3. `gcd` 함수는 재귀 (recursion) 를 사용합니다.

4. 기저 사례 (base case) 는 `y`가 `0`과 같을 때입니다. 이 경우 함수는 `x`를 반환합니다.

5. 그렇지 않으면 함수는 `y`와 `x / y`의 나머지 (remainder) 의 GCD 를 반환합니다.

6. 함수를 테스트하려면 다음 코드를 사용합니다.

```js
gcd(8, 36); // 4
gcd(...[12, 8, 32]); // 4
```
