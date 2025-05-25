# JavaScript 로 구현한 K-평균 클러스터링 알고리즘

k-평균 클러스터링 알고리즘을 사용하여 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 이 알고리즘은 주어진 데이터를 [k-평균 클러스터링](https://en.wikipedia.org/wiki/K-means_clustering) 알고리즘을 사용하여 `k`개의 클러스터로 그룹화합니다.

구현에 사용되는 단계는 다음과 같습니다.

1. `Array.from()` 및 `Array.prototype.slice()`를 사용하여 클러스터 `centroids`, `distances` 및 `classes`에 대한 적절한 변수를 초기화합니다.
2. `itr`로 표시된 대로 이전 반복에서 변경 사항이 있는 동안 `while` 루프를 사용하여 할당 및 업데이트 단계를 반복합니다.
3. `Math.hypot()`, `Object.keys()` 및 `Array.prototype.map()`을 사용하여 각 데이터 포인트와 중심점 간의 유클리드 거리 (euclidean distance) 를 계산합니다.
4. `Array.prototype.indexOf()` 및 `Math.min()`을 사용하여 가장 가까운 중심점을 찾습니다.
5. `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` 및 `Number.prototype.toFixed()`를 사용하여 새로운 중심점을 계산합니다.

```js
const kMeans = (data, k = 1) => {
  const centroids = data.slice(0, k);
  const distances = Array.from({ length: data.length }, () =>
    Array.from({ length: k }, () => 0)
  );
  const classes = Array.from({ length: data.length }, () => -1);
  let itr = true;

  while (itr) {
    itr = false;

    for (let d in data) {
      for (let c = 0; c < k; c++) {
        distances[d][c] = Math.hypot(
          ...Object.keys(data[0]).map((key) => data[d][key] - centroids[c][key])
        );
      }
      const m = distances[d].indexOf(Math.min(...distances[d]));
      if (classes[d] !== m) itr = true;
      classes[d] = m;
    }

    for (let c = 0; c < k; c++) {
      centroids[c] = Array.from({ length: data[0].length }, () => 0);
      const size = data.reduce((acc, _, d) => {
        if (classes[d] === c) {
          acc++;
          for (let i in data[0]) centroids[c][i] += data[d][i];
        }
        return acc;
      }, 0);
      for (let i in data[0]) {
        centroids[c][i] = parseFloat(Number(centroids[c][i] / size).toFixed(2));
      }
    }
  }

  return classes;
};
```

알고리즘을 테스트하려면 데이터 배열과 원하는 클러스터 수 `k`를 사용하여 `kMeans()` 함수를 호출하십시오. 이 함수는 각 데이터 포인트에 대한 클래스 할당 배열을 반환합니다.

```js
kMeans(
  [
    [0, 0],
    [0, 1],
    [1, 3],
    [2, 0]
  ],
  2
); // [0, 1, 1, 0]
```
