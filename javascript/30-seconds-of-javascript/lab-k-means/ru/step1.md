# Реализация алгоритма кластеризации k-средних на JavaScript

Для начала практики программирования с использованием алгоритма кластеризации k-средних откройте Терминал/SSH и введите `node`. Этот алгоритм группирует заданные данные в `k` кластеров с использованием алгоритма [кластеризации k-средних](https://en.wikipedia.org/wiki/K-means_clustering).

Следующие шаги используются в реализации:

1. Инициализируйте соответствующие переменные для центроидов кластеров `centroids`, расстояний `distances` и классов `classes` с использованием `Array.from()` и `Array.prototype.slice()`.
2. Повторяйте шаги назначения и обновления с использованием цикла `while`, пока не будут обнаружены изменения в предыдущей итерации, как показано `itr`.
3. Вычислите евклидово расстояние между каждой точкой данных и центроидом с использованием `Math.hypot()`, `Object.keys()` и `Array.prototype.map()`.
4. Найдите ближайший центроид с использованием `Array.prototype.indexOf()` и `Math.min()`.
5. Вычислите новые центроиды с использованием `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` и `Number.prototype.toFixed()`.

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

Для тестирования алгоритма вызовите функцию `kMeans()` с массивом данных и желаемым количеством кластеров `k`. Функция возвращает массив назначений классов для каждой точки данных.

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
