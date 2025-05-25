# Função para Retornar N Elementos Mínimos de um Array

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Use a função `minN` para retornar os `n` elementos mínimos de um array.

Veja como usar a função:

- Use `Array.prototype.sort()` e o operador spread (`...`) para criar um clone raso (shallow clone) do array e ordená-lo em ordem crescente.
- Use `Array.prototype.slice()` para obter o número especificado de elementos.
- Se você omitir o segundo argumento, `n`, a função retornará um array de um elemento.
- Se `n` for maior ou igual ao comprimento do array fornecido, a função retornará o array original, ordenado em ordem crescente.

```js
const minN = (arr, n = 1) => [...arr].sort((a, b) => a - b).slice(0, n);
```

Aqui estão alguns exemplos:

```js
minN([1, 2, 3]); // [1]
minN([1, 2, 3], 2); // [1, 2]
```
