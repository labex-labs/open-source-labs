# Como Filtrar Valores Únicos em um Array usando JavaScript

Para filtrar valores únicos em um array usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o construtor `Set` e o operador spread (`...`) para criar um array dos valores únicos no seu array original.
3.  Use `Array.prototype.filter()` para criar um array contendo apenas os valores não únicos.
4.  Defina uma função chamada `filterUnique` que recebe um array como argumento e aplica os passos acima a ele.
5.  Chame a função `filterUnique` com seu array como argumento.

Aqui está um trecho de código de exemplo para conseguir isso:

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

No trecho de código acima, a função `filterUnique` recebe um array e aplica o construtor `Set` e o método `Array.prototype.filter()` a ele para retornar um array com apenas os valores não únicos.
