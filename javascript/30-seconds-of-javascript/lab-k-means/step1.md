# K-Means Clustering Algorithm Implementation in JavaScript

To start practicing coding using the k-means clustering algorithm, open the Terminal/SSH and type `node`. This algorithm groups the given data into `k` clusters, using the [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) algorithm.

The following steps are used in the implementation:

1. Initialize appropriate variables for the cluster `centroids`, `distances` and `classes` using `Array.from()` and `Array.prototype.slice()`.
2. Repeat the assignment and update steps using a `while` loop as long as there are changes in the previous iteration, as indicated by `itr`.
3. Calculate the euclidean distance between each data point and centroid using `Math.hypot()`, `Object.keys()` and `Array.prototype.map()`.
4. Find the closest centroid using `Array.prototype.indexOf()` and `Math.min()`.
5. Calculate the new centroids using `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` and `Number.prototype.toFixed()`.

```js
const kMeans = (data, k = 1) => {
  const centroids = data.slice(0, k);
  const distances = Array.from({ length: data.length }, () =>
    Array.from({ length: k }, () => 0),
  );
  const classes = Array.from({ length: data.length }, () => -1);
  let itr = true;

  while (itr) {
    itr = false;

    for (let d in data) {
      for (let c = 0; c < k; c++) {
        distances[d][c] = Math.hypot(
          ...Object.keys(data[0]).map(
            (key) => data[d][key] - centroids[c][key],
          ),
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

To test the algorithm, call the `kMeans()` function with a data array and the desired number of clusters `k`. The function returns an array of class assignments for each data point.

```js
kMeans(
  [
    [0, 0],
    [0, 1],
    [1, 3],
    [2, 0],
  ],
  2,
); // [0, 1, 1, 0]
```
