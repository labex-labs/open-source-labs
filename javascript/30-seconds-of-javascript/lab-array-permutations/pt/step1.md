# Como Gerar Todas as Permutações de um Array

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está um algoritmo que gera todas as permutações dos elementos de um array (mesmo que contenha duplicatas). Siga estes passos para implementá-lo:

1. Use recursão.
2. Para cada elemento no array fornecido, crie todas as permutações parciais para o restante de seus elementos.
3. Use `Array.prototype.map()` para combinar o elemento com cada permutação parcial, e então `Array.prototype.reduce()` para combinar todas as permutações em um array.
4. Os casos base são para arrays com um comprimento de `2` ou `1`.
5. Esteja ciente de que o tempo de execução desta função aumenta exponencialmente com cada elemento do array. Qualquer coisa com mais de 8 a 10 entradas pode fazer com que seu navegador congele ao tentar resolver todas as diferentes combinações.

Aqui está o código:

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val
        ])
      ),
    []
  );
};
```

Você pode testar o código chamando a função `permutations()` com um argumento de array:

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
