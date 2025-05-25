# 벡터 각도 계산

두 벡터 사이의 각도 (theta) 를 계산하려면 다음 단계를 따르세요:

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`, `Math.pow()` 및 `Math.sqrt()`를 사용하여 각 벡터의 크기 (magnitude) 와 두 벡터의 스칼라 곱 (scalar product) 을 계산합니다.
3. `Math.acos()`를 사용하여 아크코사인 (arccosine) 을 계산하고 theta 값을 얻습니다.

다음은 예시 코드 조각입니다:

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

이 함수는 두 개의 배열 (`x`와 `y`) 을 인수로 받아 두 벡터 사이의 각도 (라디안 단위) 를 반환합니다.
