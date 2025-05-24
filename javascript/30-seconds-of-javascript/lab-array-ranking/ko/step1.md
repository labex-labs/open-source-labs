# 배열 랭킹 (Ranking Arrays)

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 이 함수는 비교 함수 (comparator function) 를 기반으로 배열의 랭킹을 계산합니다.

이 함수를 사용하려면 다음을 수행할 수 있습니다.

- 제공된 비교 함수를 사용하여 각 요소를 랭크 (rank) 에 매핑하기 위해 `Array.prototype.map()` 및 `Array.prototype.filter()`를 사용합니다.

다음은 사용 예시입니다.

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

예시:

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
