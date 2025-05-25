# Removendo Elementos de um Array do Final até que uma Condição seja Atendida

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Esta função remove elementos do final de um array até que a função passada retorne `true` e, em seguida, retorna os elementos removidos.

Veja como funciona:

- Primeiro, crie uma cópia invertida do array usando o operador spread (`...`) e `Array.prototype.reverse()`.
- Em seguida, itere sobre a cópia invertida usando um loop `for...of` sobre `Array.prototype.entries()` até que o valor retornado da função seja truthy.
- Depois disso, retorne os elementos removidos usando `Array.prototype.slice()`.
- A função de callback, `fn`, aceita um único argumento que é o valor do elemento.

Aqui está o código:

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Aqui está um exemplo de como usar esta função:

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
