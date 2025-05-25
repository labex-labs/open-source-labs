# Removendo Elementos de um Array do Fim até que uma Condição seja Atendida

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está uma função que remove elementos do final de um array até que a função passada retorne `false`. Em seguida, ela retorna os elementos removidos.

Para usá-la, crie uma cópia invertida do array usando o operador spread (`...`) e `Array.prototype.reverse()`. Em seguida, itere sobre a cópia invertida usando um loop `for...of` sobre `Array.prototype.entries()` até que o valor retornado da função seja falsy.

A função de callback, `fn`, aceita um único argumento que é o valor do elemento. Finalmente, retorne os elementos removidos usando `Array.prototype.slice()`.

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Aqui está um exemplo de como usar a função:

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
