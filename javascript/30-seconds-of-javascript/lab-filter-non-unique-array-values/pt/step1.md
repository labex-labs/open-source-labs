# Como Filtrar Valores Não Únicos em um Array em JavaScript

Para filtrar valores não únicos em um array em JavaScript, você pode criar um novo array com apenas os valores únicos. Veja como:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o construtor `Set` e o operador spread (`...`) para criar um array dos valores únicos no array original.
3.  Use `Array.prototype.filter()` para criar um array contendo apenas os valores únicos.

Aqui está um exemplo de função que faz isso:

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

Você pode usar esta função com qualquer array para filtrar os valores não únicos. Por exemplo:

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
