# 매핑된 배열의 평균 계산 지침

배열의 평균을 계산하려면 제공된 함수를 사용하여 각 요소를 새 값으로 매핑할 수 있습니다. 다음은 단계별 지침입니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()`을 사용하여 각 요소를 `fn`에서 반환된 값으로 매핑합니다.
3. `Array.prototype.reduce()`를 사용하여 각 매핑된 값을 `0`으로 초기화된 누산기에 더합니다.
4. 평균을 구하기 위해 결과 배열을 길이로 나눕니다.

다음은 사용할 수 있는 코드입니다.

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

다음 예제를 사용하여 이 함수를 테스트할 수 있습니다.

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
