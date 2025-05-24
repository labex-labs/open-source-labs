# Função de Diferença Simétrica Única de Array

Para praticar a codificação, abra o Terminal/SSH e digite `node`. A função a seguir retorna a diferença simétrica única entre dois arrays. Ela remove valores duplicados de qualquer um dos arrays.

Para conseguir isso, use `Array.prototype.filter()` e `Array.prototype.includes()` em cada array para remover valores contidos no outro. Crie um `Set` a partir dos resultados para remover valores duplicados.

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

Use a função como mostrado abaixo:

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
