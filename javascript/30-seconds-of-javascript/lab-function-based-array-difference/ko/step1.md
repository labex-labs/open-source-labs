# 함수 기반으로 배열에서 값 필터링하는 방법

주어진 비교 함수를 기반으로 배열에서 모든 값을 필터링하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.filter()` 및 `Array.prototype.findIndex()`를 사용하여 적절한 값을 찾습니다.
3. 마지막 인수 `comp`를 생략하여 기본 엄격한 동등성 비교자 (strict equality comparator) 를 사용합니다.
4. 다음 코드를 사용합니다.

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. 다음 예제를 사용하여 함수를 테스트합니다.

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // Expected output: [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // Expected output: [1.2]
```
