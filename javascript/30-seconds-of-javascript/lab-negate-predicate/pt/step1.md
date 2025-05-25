# Como Negar uma Função Predicado em JavaScript

Para negar uma função predicado em JavaScript, você pode usar o operador `!`. Para fazer isso, você pode criar uma função de ordem superior (higher-order function) chamada `negate` que recebe uma função predicado e aplica o operador `!` a ela com seus argumentos. Aqui está um exemplo de como implementar `negate`:

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

Você pode então usar `negate` para negar qualquer função predicado. Aqui está um exemplo de como usar `negate` para filtrar números pares de um array:

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

Neste exemplo, `isEven` é uma função predicado que verifica se um número é par. Em seguida, usamos `negate` para criar uma nova função predicado chamada `isOdd` que verifica se um número é ímpar, negando `isEven`. Finalmente, usamos `isOdd` com o método `filter` para filtrar os números pares do array.
