# JavaScript 에서 가중 평균 계산 방법

JavaScript 에서 두 개 이상의 숫자의 가중 평균을 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`를 사용하여 값의 가중 합과 가중치의 합을 구합니다.
3. 값의 가중 합을 가중치의 합으로 나누어 가중 평균을 구합니다.

다음은 `weightedAverage` 함수의 JavaScript 코드입니다.

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

`weightedAverage` 함수를 사용하여 숫자 배열과 가중치 배열의 가중 평균을 다음과 같이 계산할 수 있습니다.

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
