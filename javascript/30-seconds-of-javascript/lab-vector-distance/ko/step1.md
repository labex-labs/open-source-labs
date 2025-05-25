# 벡터 거리 계산

두 벡터 간의 거리를 계산하려면 다음 단계를 따르세요.

1. 코딩 연습을 시작하기 위해 터미널/SSH 를 엽니다.
2. `node`를 입력하여 시작합니다.
3. `Array.prototype.reduce()`, `Math.pow()`, 그리고 `Math.sqrt()`를 사용하여 벡터 간의 유클리드 거리 (Euclidean distance) 를 구합니다.
4. 아래에 표시된 `vectorDistance` 공식을 적용합니다.

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. 다음 형식으로 두 개의 벡터를 입력하여 공식을 테스트합니다: `vectorDistance([10, 0, 5], [20, 0, 10]);`
6. 출력은 두 벡터 간의 거리인 `11.180339887498949`가 됩니다.
