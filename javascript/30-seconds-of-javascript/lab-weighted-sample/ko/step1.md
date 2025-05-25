# JavaScript 에서 가중치 샘플링을 배열에서 얻는 방법

제공된 가중치를 기반으로 배열에서 요소를 무작위로 얻으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`를 사용하여 `weights`의 각 값에 대한 부분 합의 배열을 생성합니다.
3. `Math.random()`을 사용하여 난수를 생성하고 `Array.prototype.findIndex()`를 사용하여 이전에 생성된 배열을 기반으로 올바른 인덱스를 찾습니다.
4. 마지막으로, 생성된 인덱스를 사용하여 `arr`의 요소를 반환합니다.

다음은 이를 달성하기 위한 코드입니다.

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

배열과 해당 가중치를 인수로 전달하여 이 함수를 테스트할 수 있습니다.

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
