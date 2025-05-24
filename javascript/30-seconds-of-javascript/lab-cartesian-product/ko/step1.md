# 데카르트 곱 (Cartesian Product)

두 배열의 데카르트 곱을 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`, `Array.prototype.map()` 및 스프레드 연산자 (`...`) 를 사용하여 두 배열에서 가능한 모든 요소 쌍을 생성합니다.
3. 다음 코드를 사용합니다.

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

예시:

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

이렇게 하면 두 배열의 요소에서 가능한 모든 조합이 생성됩니다.
