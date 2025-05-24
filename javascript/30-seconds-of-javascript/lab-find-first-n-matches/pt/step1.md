# Como Encontrar as Primeiras N Correspondências

Para encontrar os primeiros `n` elementos que atendem a um determinado critério, use a função `findFirstN`. Veja como:

1. Abra o Terminal/SSH.
2. Digite `node` para começar a praticar a codificação.
3. Use a função `findFirstN`, passando o array a ser pesquisado, uma função de correspondência (matching function) e o número de correspondências a serem encontradas (se não especificado, o padrão é 1).
4. A função `matcher` será executada para cada elemento do `arr`, e se retornar um valor verdadeiro (truthy), esse elemento será adicionado ao array de resultados.
5. Se o array `res` atingir um comprimento de `n`, a função retornará o array de resultados.
6. Se nenhuma correspondência for encontrada, um array vazio será retornado.

Aqui está o código para a função `findFirstN`:

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

E aqui estão alguns exemplos de como usá-la:

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
