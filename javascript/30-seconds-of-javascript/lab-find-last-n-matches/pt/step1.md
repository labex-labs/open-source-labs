# Instruções para encontrar as Últimas N Correspondências

Para encontrar os últimos `n` elementos que correspondem a uma determinada condição, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a função `findLastN` fornecida abaixo.
3.  Forneça um array `arr` e uma função `matcher` que retorna um valor truthy para os elementos que você deseja corresponder.
4.  Opcionalmente, você também pode fornecer o número `n` de correspondências que deseja retornar (o padrão é 1).
5.  A função executará a função `matcher` para cada elemento de `arr` usando um loop `for`, começando pelo último elemento.
6.  Se um elemento corresponder à condição `matcher`, ele será adicionado ao array de resultados usando `Array.prototype.unshift()`, que adiciona elementos ao início do array.
7.  Quando o comprimento do array de resultados for igual a `n`, a função retornará os resultados.
8.  Se não houver correspondências ou se `n` for maior que o número de correspondências, um array vazio será retornado.

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Aqui estão alguns exemplos de como usar a função `findLastN`:

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
