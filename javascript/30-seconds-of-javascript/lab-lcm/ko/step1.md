# 최소 공배수 계산

두 개 이상의 숫자의 최소 공배수를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 최대 공약수 (GCD) 공식과 `lcm(x, y) = x * y / gcd(x, y)` 공식을 사용하여 최소 공배수를 결정합니다.
3. GCD 공식은 재귀 (recursion) 를 사용합니다.
4. JavaScript 에서 다음 코드를 구현합니다.

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

사용 예시:

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
