# Algoritmo de Ordenação por Inserção em JavaScript

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Este algoritmo ordena um array de números usando o método de ordenação por inserção (insertion sort). Siga estes passos para implementar este algoritmo:

1.  Use `Array.prototype.reduce()` para iterar sobre todos os elementos no array fornecido.
2.  Se o `length` (comprimento) do acumulador for `0`, adicione o elemento atual a ele.
3.  Use `Array.prototype.some()` para iterar sobre os resultados no acumulador até que a posição correta seja encontrada.
4.  Use `Array.prototype.splice()` para inserir o elemento atual no acumulador.

Aqui está o código para implementar a ordenação por inserção em JavaScript:

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

Você pode testar o algoritmo com o seguinte código:

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
