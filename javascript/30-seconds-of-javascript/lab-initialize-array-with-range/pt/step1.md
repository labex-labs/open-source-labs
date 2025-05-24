# Função para Inicializar Array com Intervalo

Para inicializar um array com um intervalo de números, use a seguinte função:

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

Esta função recebe três argumentos: `end` (obrigatório), `start` (opcional, valor padrão é `0`), e `step` (opcional, valor padrão é `1`). Ela retorna um array contendo os números no intervalo especificado, onde `start` e `end` são inclusivos com sua diferença comum `step`.

Para usar esta função, simplesmente chame-a com os parâmetros de intervalo desejados:

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

Esta função usa `Array.from()` para criar um array do comprimento desejado, e então uma função map para preencher o array com os valores desejados no intervalo dado. Se você omitir o segundo argumento, `start`, ele usará um valor padrão de `0`. Se você omitir o último argumento, `step`, ele usará um valor padrão de `1`.
