# JavaScript 에서 가장 성능 좋은 함수를 찾는 방법

JavaScript 에서 가장 성능 좋은 함수를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()`을 사용하여 각 값이 `iterations` 횟수만큼 함수를 실행하는 데 걸린 총 시간인 배열을 생성합니다.
3. `performance.now()` 값의 전후 차이를 사용하여 밀리초 단위의 총 시간을 높은 정확도로 얻습니다.
4. `Math.min()`을 사용하여 최소 실행 시간을 찾고, 가장 성능 좋은 함수의 인덱스에 해당하는 해당 최소 시간의 인덱스를 반환합니다.
5. 두 번째 인수 `iterations`를 생략하면 함수는 기본값인 `10000` 반복 횟수를 사용합니다.
6. 반복 횟수가 많을수록 결과의 신뢰성은 높아지지만 시간이 더 오래 걸린다는 점을 명심하세요.

다음은 코드 스니펫 예시입니다.

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

이 함수를 사용하려면 함수 배열을 첫 번째 인수로, 반복 횟수를 두 번째 인수로 전달합니다 (선택 사항). 예를 들어:

```js
mostPerformant([
  () => {
    // Loops through the entire array before returning `false`
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // Only needs to reach index `1` before returning `false`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
