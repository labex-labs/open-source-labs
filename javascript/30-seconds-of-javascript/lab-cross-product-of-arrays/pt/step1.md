# Criando um Produto Cruzado de Array em JavaScript

Para criar um produto cruzado de array em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()`, `Array.prototype.map()` e `Array.prototype.concat()` para produzir cada par possível a partir dos elementos dos dois arrays.
3.  A função `xProd()` recebe dois arrays como argumentos e cria um novo array a partir dos dois fornecidos, criando cada par possível a partir dos arrays.
4.  Aqui está um exemplo da função `xProd()` em ação:

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

Isso retornará um array contendo todos os pares possíveis de elementos dos dois arrays de entrada.
