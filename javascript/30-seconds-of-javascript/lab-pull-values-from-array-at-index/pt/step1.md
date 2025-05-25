# Como Extrair Valores de um Array por Índice

Para extrair valores específicos de um array em determinados índices, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.filter()` e `Array.prototype.includes()` para filtrar os valores que não são necessários e armazená-los em um novo array chamado `removed`.
3.  Defina `Array.prototype.length` como `0` para mutar o array original, redefinindo seu comprimento.
4.  Use `Array.prototype.push()` para repovoar o array original com apenas os valores extraídos.
5.  Use `Array.prototype.push()` para manter o controle dos valores removidos.
6.  A função `pullAtIndex` recebe dois argumentos: o array original e um array de índices a serem extraídos.
7.  A função retorna um array de valores removidos.

Exemplo de uso:

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ] , pulled = [ 'b', 'd' ]
```
