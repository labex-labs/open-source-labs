# Como Encontrar o Item Mais Longo em um Array

Para encontrar o item mais longo em um array, abra o Terminal/SSH e digite `node`. A função recebe qualquer número de objetos iteráveis ou objetos com uma propriedade `length` e retorna o mais longo. Ela usa `Array.prototype.reduce()` para comparar o comprimento dos objetos e encontrar o mais longo. Se múltiplos objetos tiverem o mesmo comprimento, a função retorna o primeiro. Se nenhum argumento for fornecido, ela retorna `undefined`.

Aqui está o código:

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

Você pode usar a função assim:

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
