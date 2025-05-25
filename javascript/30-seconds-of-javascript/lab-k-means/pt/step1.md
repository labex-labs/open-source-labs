# Implementação do Algoritmo de Agrupamento K-Means em JavaScript

Para começar a praticar a codificação utilizando o algoritmo de agrupamento k-means, abra o Terminal/SSH e digite `node`. Este algoritmo agrupa os dados fornecidos em `k` clusters, utilizando o algoritmo [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering).

As seguintes etapas são utilizadas na implementação:

1.  Inicialize as variáveis apropriadas para os `centroids` (centróides) dos clusters, `distances` (distâncias) e `classes` (classes) utilizando `Array.from()` e `Array.prototype.slice()`.
2.  Repita as etapas de atribuição e atualização utilizando um loop `while` enquanto houver mudanças na iteração anterior, conforme indicado por `itr`.
3.  Calcule a distância euclidiana entre cada ponto de dados e o centróide utilizando `Math.hypot()`, `Object.keys()` e `Array.prototype.map()`.
4.  Encontre o centróide mais próximo utilizando `Array.prototype.indexOf()` e `Math.min()`.
5.  Calcule os novos centróides utilizando `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` e `Number.prototype.toFixed()`.

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

Para testar o algoritmo, chame a função `kMeans()` com um array de dados e o número desejado de clusters `k`. A função retorna um array de atribuições de classe para cada ponto de dados.

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
