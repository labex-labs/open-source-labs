# Como Inicializar um Array com uma Sequência Invertida em JavaScript

Para inicializar um array com uma sequência invertida em JavaScript, use a seguinte função:

```js
const initializeArrayWithRangeRight = (end, start = 0, step = 1) =>
  Array.from({ length: Math.ceil((end + 1 - start) / step) }).map(
    (v, i, arr) => (arr.length - i - 1) * step + start
  );
```

Esta função cria um array contendo os números no intervalo especificado em ordem inversa. Os parâmetros `start` e `end` são inclusivos, e o parâmetro `step` especifica a diferença comum entre os números no intervalo.

Para usar a função, chame-a com os valores `end`, `start` e `step` desejados como argumentos, assim:

```js
initializeArrayWithRangeRight(5); // [5, 4, 3, 2, 1, 0]
initializeArrayWithRangeRight(7, 3); // [7, 6, 5, 4, 3]
initializeArrayWithRangeRight(9, 0, 2); // [8, 6, 4, 2, 0]
```

Se você omitir o argumento `start`, ele assume o valor padrão de `0`. Se você omitir o argumento `step`, ele assume o valor padrão de `1`.
