# K 近邻算法

若要使用 K 近邻算法，请遵循以下步骤：

1. 打开终端/SSH 并输入`node`。
2. 使用[K 近邻](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)算法相对于已标记数据集对一个数据点进行分类。
3. 使用`Array.prototype.map()`将`data`映射到对象。每个对象都包含该元素与`point`之间的欧几里得距离（使用`Math.hypot()`、`Object.keys()`计算得出）及其`label`。
4. 使用`Array.prototype.sort()`和`Array.prototype.slice()`获取`point`的`k`个最近邻。
5. 结合使用`Array.prototype.reduce()`、`Object.keys()`和`Array.prototype.indexOf()`来找出其中出现频率最高的`label`。

以下是实现 K 近邻算法的示例代码：

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

以下是使用该代码的方法：

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
