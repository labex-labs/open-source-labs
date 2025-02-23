# Алгоритм k-ближайших соседей

Для использования Алгоритма k-ближайших соседей следуйте шагам:

1. Откройте Терминал/SSH и введите `node`.
2. Классифицируйте точку данных относительно помеченного набора данных с использованием алгоритма [k-ближайших соседей](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).
3. Сопоставьте `data` с объектами с использованием `Array.prototype.map()`. Каждый объект содержит евклидово расстояние элемента от `point`, вычисленное с использованием `Math.hypot()`, `Object.keys()` и его `label`.
4. Используйте `Array.prototype.sort()` и `Array.prototype.slice()`, чтобы получить `k` ближайших соседей `point`.
5. Используйте `Array.prototype.reduce()` в сочетании с `Object.keys()` и `Array.prototype.indexOf()`, чтобы найти наиболее часто встречающийся `label` среди них.

Вот пример кода, который реализует Алгоритм k-ближайших соседей:

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

Вот, как использовать этот код:

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
