# 유클리드 거리 계산 (Euclidean Distance Calculation)

임의의 차원에서 두 점 사이의 거리를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`와 `Array.prototype.map()`을 사용하여 각 좌표를 두 점 간의 차이에 매핑합니다.
3. `Math.hypot()`을 사용하여 두 점 사이의 유클리드 거리 (Euclidean Distance) 를 계산합니다.

다음은 시작하는 데 도움이 되는 코드 스니펫입니다.

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

다음 샘플 입력을 사용하여 함수를 테스트해 볼 수 있습니다.

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
