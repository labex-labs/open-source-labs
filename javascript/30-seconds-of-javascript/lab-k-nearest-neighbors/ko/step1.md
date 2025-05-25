# K-최근접 이웃 (K-Nearest Neighbors) 알고리즘

K-최근접 이웃 알고리즘을 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. [k-최근접 이웃](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) 알고리즘을 사용하여 레이블된 데이터 세트를 기준으로 데이터 포인트를 분류합니다.
3. `Array.prototype.map()`을 사용하여 `data`를 객체에 매핑합니다. 각 객체는 `Math.hypot()`, `Object.keys()` 및 해당 `label`을 사용하여 계산된, `point`에서 요소까지의 유클리드 거리 (Euclidean distance) 를 포함합니다.
4. `Array.prototype.sort()` 및 `Array.prototype.slice()`를 사용하여 `point`의 `k`개의 가장 가까운 이웃을 가져옵니다.
5. `Array.prototype.reduce()`를 `Object.keys()` 및 `Array.prototype.indexOf()`와 함께 사용하여 가장 빈번한 `label`을 찾습니다.

다음은 K-최근접 이웃 알고리즘을 구현하는 코드 예시입니다.

```js
const kNearestNeighbors = (data, labels, point, k = 3) => {
  const kNearest = data
    .map((el, i) => ({
      dist: Math.hypot(...Object.keys(el).map((key) => point[key] - el[key])),
      label: labels[i]
    }))
    .sort((a, b) => a.dist - b.dist)
    .slice(0, k);

  return kNearest.reduce(
    (acc, { label }, i) => {
      acc.classCounts[label] =
        Object.keys(acc.classCounts).indexOf(label) !== -1
          ? acc.classCounts[label] + 1
          : 1;
      if (acc.classCounts[label] > acc.topClassCount) {
        acc.topClassCount = acc.classCounts[label];
        acc.topClass = label;
      }
      return acc;
    },
    {
      classCounts: {},
      topClass: kNearest[0].label,
      topClassCount: 0
    }
  ).topClass;
};
```

다음은 코드를 사용하는 방법입니다.

```js
const data = [
  [0, 0],
  [0, 1],
  [1, 3],
  [2, 0]
];
const labels = [0, 1, 1, 0];

kNearestNeighbors(data, labels, [1, 2], 2); // 1
kNearestNeighbors(data, labels, [1, 0], 2); // 0
```
