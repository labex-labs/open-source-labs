# Transpor uma Matriz em JavaScript

Para transpor um array bidimensional em JavaScript, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.map()` para criar a transposição do array bidimensional fornecido. O método `map()` cria um novo array com os resultados da chamada de uma função fornecida em cada elemento do array.
3. A função fornecida deve receber dois argumentos: o elemento atual do array e seu índice. Neste caso, precisamos apenas do índice para criar a transposição.
4. Use o índice para acessar os elementos correspondentes em cada linha do array bidimensional e crie um novo array com esses elementos. Esta será a nova linha no array transposto.
5. Repita o passo anterior para cada coluna no array bidimensional para criar o array transposto completo.

Aqui está o código para transpor um array bidimensional em JavaScript:

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
