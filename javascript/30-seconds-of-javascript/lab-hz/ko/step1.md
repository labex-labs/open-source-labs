# 함수 주파수 계산

초당 함수 실행 빈도 (hz/헤르츠) 를 측정하려면 `hz` 함수를 사용하십시오. 다음 단계를 수행하여 이를 수행할 수 있습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `performance.now()`를 사용하여 반복 루프 전후의 밀리초 차이를 구하여 함수를 `iterations` 횟수만큼 실행하는 데 걸린 시간을 계산합니다.
3. 밀리초를 초로 변환하고 경과 시간으로 나누어 초당 사이클 수를 반환합니다.
4. 기본값인 100 번의 반복을 사용하려면 두 번째 인수 `iterations`를 생략합니다.

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

다음은 `hz` 함수를 사용하여 10,000 개의 숫자로 구성된 배열의 합계를 계산하는 두 함수의 성능을 비교하는 예입니다.

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

이 예에서 `sumReduce`는 함수 실행 빈도가 낮기 때문에 `sumForLoop`보다 빠릅니다.
