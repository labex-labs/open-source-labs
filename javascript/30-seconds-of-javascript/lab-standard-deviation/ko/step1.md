# 표준 편차 (Standard Deviation)

JavaScript 에서 숫자 배열의 표준 편차를 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 아래 제공된 함수 `standardDeviation(arr, usePopulation = false)`를 사용합니다.
3. 숫자 배열을 함수의 첫 번째 인수로 전달합니다.
4. 두 번째 인수 `usePopulation`을 생략하면 표본 표준 편차를 얻습니다. 모집단 표준 편차를 얻으려면 이 값을 `true`로 설정합니다.

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

사용 예시:

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (sample)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (population)
```
