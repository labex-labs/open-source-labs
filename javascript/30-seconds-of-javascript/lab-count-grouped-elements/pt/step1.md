# Como Agrupar e Contar Elementos em um Array Usando JavaScript

Para agrupar e contar elementos em um array usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.map()` para mapear os valores de um array para uma função ou nome de propriedade.
3.  Use o método `Array.prototype.reduce()` para criar um objeto onde as chaves são produzidas a partir dos resultados mapeados.
4.  Crie uma função chamada `countBy` que recebe um array e uma função como argumentos.
5.  Dentro da função `countBy`, use um operador ternário para verificar se o argumento passado é uma função ou um nome de propriedade. Se for uma função, use-a como a função de mapeamento. Se for um nome de propriedade, acesse essa propriedade dos elementos do array.
6.  Use o método `reduce()` para criar um objeto onde cada chave representa um elemento único no array e seu valor é o número de vezes que ele aparece no array.

Aqui está o código:

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

Você pode testar a função `countBy` com os seguintes exemplos:

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
