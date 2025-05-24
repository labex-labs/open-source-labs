# Removendo Elementos de Array da Esquerda

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está uma função que cria um novo array com um número especificado de elementos removidos da esquerda:

```js
const drop = (arr, n = 1) => arr.slice(n);
```

A função usa `Array.prototype.slice()` para remover o número especificado de elementos da esquerda. Se você omitir o último argumento, `n`, a função usará um valor padrão de `1`.

Aqui estão alguns exemplos de como usar a função `drop`:

```js
drop([1, 2, 3]); // [2, 3]
drop([1, 2, 3], 2); // [3]
drop([1, 2, 3], 42); // []
```
