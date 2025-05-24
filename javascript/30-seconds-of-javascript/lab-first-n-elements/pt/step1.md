# Como Obter os Primeiros N Elementos de um Array em JavaScript

Para obter os primeiros `n` elementos de um array em JavaScript, você pode usar o método `Array.prototype.slice()`. Veja como:

```js
const firstN = (arr, n) => arr.slice(0, n);
```

Neste trecho de código, `arr` representa o array do qual você deseja extrair os elementos, e `n` representa o número de elementos que você deseja extrair. O método `slice()` recebe dois argumentos: o índice inicial (que é `0` neste caso) e o índice final (que é `n`). O método retorna um novo array contendo os elementos extraídos.

Aqui está um exemplo de como usar a função `firstN()`:

```js
firstN(["a", "b", "c", "d"], 2); // ['a', 'b']
```

Isso retornará os dois primeiros elementos do array `['a', 'b', 'c', 'd']`, que são `['a', 'b']`.
