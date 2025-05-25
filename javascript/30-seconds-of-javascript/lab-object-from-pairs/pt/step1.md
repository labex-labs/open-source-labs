# Criando um Objeto a partir de Pares Chave-Valor

Para criar um objeto a partir de pares chave-valor, use a função `objectFromPairs`.

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- A função usa `Array.prototype.reduce()` para criar e combinar pares chave-valor.
- Para uma implementação mais simples, você também pode usar [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries).

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

Exemplo de uso:

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
